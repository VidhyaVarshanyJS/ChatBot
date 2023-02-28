from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import operator

class ParseFloatMapper:
    def __call__(self, value: Text) -> float:
        try:
            return float(value)
        except ValueError:
            return None

class ActionPerformMathOperation(Action):
    def name(self) -> Text:
        return "action_perform_math_operation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        first_operand = tracker.get_slot("first_operand")
        second_operand = tracker.get_slot("second_operand")
        operation = tracker.get_slot("operation")

        try:
            if operation == "addition":
                result = operator.add(first_operand, second_operand)
                dispatcher.utter_message(text=f"The sum of {first_operand} and {second_operand} is {result}")
            elif operation == "subtraction":
                result = operator.sub(first_operand, second_operand)
                dispatcher.utter_message(text=f"The difference between {first_operand} and {second_operand} is {result}")
            elif operation == "multiplication":
                result = operator.mul(first_operand, second_operand)
                dispatcher.utter_message(text=f"The product of {first_operand} and {second_operand} is {result}")
            elif operation == "division":
                if second_operand == 0:
                    dispatcher.utter_message(template="utter_division_by_zero")
                else:
                    result = operator.truediv(first_operand, second_operand)
                    dispatcher.utter_message(text=f"The division of {first_operand} by {second_operand} is {result:.2f}")
            
        except:
                dispatcher.utter_message(template="utter_invalid_input")
                return []

class ActionCheckDivisionByZero(Action):
    def name(self) -> Text:
        return "action_check_division_by_zero"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_division_by_zero")
        return [SlotSet("second_operand", None)]
    





# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet


# class ActionMathOperation(Action):

#     def name(self) -> Text:
#         return "action_math_operation"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         first_operand = tracker.get_slot('first_operand')
#         second_operand = tracker.get_slot('second_operand')
#         operation = tracker.get_slot('operation')

#         if not first_operand or not second_operand:
#             dispatcher.utter_template("utter_ask_first_operand", tracker)
#             return [SlotSet("operation", operation)]

#         if not operation:
#             dispatcher.utter_template("utter_ask_operation", tracker)
#             return [SlotSet("first_operand", first_operand), SlotSet("second_operand", second_operand)]

#         if operation == 'add':
#             result = float(first_operand) + float(second_operand)
#         elif operation == 'subtract':
#             result = float(first_operand) - float(second_operand)
#         elif operation == 'multiply':
#             result = float(first_operand) * float(second_operand)
#         elif operation == 'divide':
#             result = float(first_operand) / float(second_operand)
#         else:
#             dispatcher.utter_message("I'm sorry, I didn't understand the operation.")
#             return []

#         dispatcher.utter_template("utter_result", tracker, result=result)

#         return [SlotSet("first_operand", first_operand), SlotSet("second_operand", second_operand), SlotSet("operation", operation)]
