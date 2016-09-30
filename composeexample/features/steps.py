from lettuce import *
from django.test.client import Client

@before.all
def set_browser():
  world.browser = Client()

@step('I am in the root page')
def go_to_root(step):
  world.response = world.browser.get('/')

@step("I look at the page")
def get_content(step):
  world.content = world.response.content

@step("I see what I am looking for")
def compare_content(step):
  assert "Hello, is it me you are looking for?" in world.content