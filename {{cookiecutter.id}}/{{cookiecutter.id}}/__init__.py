from mcdreforged.api.all import *

from {{cookiecutter.id}} import my_lib


def on_load(server: PluginServerInterface, old):
    server.logger.info(server.tr('{{cookiecutter.id}}.a_message'))
    my_lib.do_something()
