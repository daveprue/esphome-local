import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import select

from .. import PIPSOLAR_COMPONENT_SCHEMA, CONF_PIPSOLAR_ID

DEPENDENCIES = ["uart"]

CONF_OUTPUT_SOURCE = "test_popup"

TYPES = [
    CONF_OUTPUT_SOURCE: select.select_schema(
	options="[Option1,Option2,Option3]" 
    ),
]

CONFIG_SCHEMA = PIPSOLAR_COMPONENT_SCHEMA.extend(
    {cv.Optional(type): schema for type, schema in TYPES.items()}
)


async def to_code(config):
    paren = await cg.get_variable(config[CONF_PIPSOLAR_ID])
    for type in TYPES:
        if type in config:
            conf = config[type]
            var = await select.new_select(conf)
            cg.add(getattr(paren, f"set_{type}")(var))
