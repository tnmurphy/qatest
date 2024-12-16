from behave import *
from theapi.stats import median, Response

@given("a list of numbers {numbers}")
def step_test_mean(context, numbers):
    context.numbers = [int(x) for x in numbers.split(",")]

@when("I calculate the median")
def step_domean(context):
    context.response = median(context.numbers)
    assert context.response.status_code == 200
    assert "median" in context.response.json()
    context.result = context.response.json()["median"]

@then("I expect the result to be {result}")
def step_expect(context, result):
    context.expected_result = float(result)
    assert context.expected_result == context.result
