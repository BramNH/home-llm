import csv
import re
from deep_translator import PonsTranslator, LingueeTranslator, GoogleTranslator
from progressbar import progressbar

SUPPORTED_DEVICES = [
    "light",
    "switch",
    "media_player",
    "climate",
    "vacuum",
    "todo",
    "blinds",
    "fan",
    "garage_door",
    "lock",
    "timer",
]

translator = GoogleTranslator(source="english", target="dutch")


def translate(phrase_to_translate) -> str:
    translated_phrase = translator.translate(phrase_to_translate, return_all=False)
    # All <device_name> blocks are also translated,
    # so place them back in english after translation.
    res = re.findall(r"\<.*?\>", phrase_to_translate)
    i = len(res) - 1
    for match in reversed(list(re.finditer(r"\<.*?\>", translated_phrase))):
        loc = match.span()
        translated_phrase = translated_phrase.replace(
            translated_phrase[loc[0] : loc[1]], res[i], 1
        )
        i -= 1
    return translated_phrase


def translate_device_names():
    print("Translating device names")
    pile_of_device_names_dutch = list()

    with open("piles/pile_of_device_names.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        pile_of_device_names = list(reader)
        pile_of_device_names = list(
            filter(
                lambda x: x["device_name"].split(".")[0] in SUPPORTED_DEVICES,
                pile_of_device_names,
            )
        )
        for device_dict in progressbar(pile_of_device_names):
            try:
                device_type, device_name = device_dict["device_name"].split(".")
                device_description = device_dict["description"]
                pile_of_device_names_dutch.append(
                    {
                        "device_name": f"{device_type}.{translator.translate(device_name, return_all=False)}",
                        "description": translator.translate(
                            device_description, return_all=False
                        ),
                    }
                )
            except KeyError as ex:
                print(ex)
    with open("piles/pile_of_device_names_dutch.csv", "w+", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["device_name", "description"])
        writer.writeheader()
        writer.writerows(pile_of_device_names_dutch)


def translate_templated_actions():
    print("Translating templated actions")
    pile_of_templated_actions_dutch = list()

    with open("piles/pile_of_templated_actions.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        pile_of_templated_actions = list(reader)
        pile_of_templated_actions = list(
            filter(
                lambda x: [t in SUPPORTED_DEVICES for t in x["device_type"].split("|")],
                pile_of_templated_actions,
            )
        )
        for actions_dict in progressbar(pile_of_templated_actions):
            try:
                pile_of_templated_actions_dutch.append(
                    {
                        "device_type": actions_dict["device_type"],
                        "service": actions_dict["service"],
                        "dutch_phrase": translate(actions_dict["english_phrase"]),
                        "multiplier": actions_dict["multiplier"],
                    }
                )
            except KeyError as ex:
                print(ex)
    with open("piles/pile_of_templated_actions_dutch.csv", "w+", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["device_type", "service", "dutch_phrase", "multiplier"]
        )
        writer.writeheader()
        writer.writerows(pile_of_templated_actions_dutch)


def translate_specific_actions():
    print("Translating specific actions")
    pile_of_specific_actions_dutch = list()

    with open("piles/pile_of_specific_actions.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        pile_of_specific_actions = list(reader)
        pile_of_specific_actions = list(
            filter(
                lambda x: x["service_name"].split(".")[0] in SUPPORTED_DEVICES,
                pile_of_specific_actions,
            )
        )
        for actions_dict in progressbar(pile_of_specific_actions):
            try:
                pile_of_specific_actions_dutch.append(
                    {
                        "service_name": actions_dict["service_name"],
                        "device_name": translator.translate(
                            actions_dict["device_name"], return_all=False
                        ),
                        "dutch_phrase": translator.translate(
                            actions_dict["english_phrase"], return_all=False
                        ),
                    }
                )
            except KeyError as ex:
                print(ex)
    with open("piles/pile_of_specific_actions_dutch.csv", "w+", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["service_name", "device_name", "dutch_phrase"]
        )
        writer.writeheader()
        writer.writerows(pile_of_specific_actions_dutch)


def translate_status_requests():
    print("Translating status requests")
    pile_of_status_requests_dutch = list()

    with open("piles/pile_of_status_requests.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        pile_of_status_requests = list(reader)
        pile_of_status_requests = list(
            filter(
                lambda x: x["device_type"] in SUPPORTED_DEVICES,
                pile_of_status_requests,
            )
        )
        for request_dict in progressbar(pile_of_status_requests):
            try:
                pile_of_status_requests_dutch.append(
                    {
                        "device_type": request_dict["device_type"],
                        "state": request_dict["state"],
                        "dutch_phrase": translate(request_dict["english_phrase"]),
                        "assistant_response": translate(request_dict["assistant_response"]),
                    }
                )
            except KeyError as ex:
                print(ex)
    with open("piles/pile_of_status_requests_dutch.csv", "w+", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["device_type", "state", "dutch_phrase", "assistant_response"],
        )
        writer.writeheader()
        writer.writerows(pile_of_status_requests_dutch)

def translate_durations():
    print("Translating durations")
    pile_of_durations_dutch = list()

    with open("piles/pile_of_durations.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        pile_of_durations = list(reader)
        for duration_dict in progressbar(pile_of_durations):
            try:
                pile_of_durations_dutch.append(
                    {
                        "duration": duration_dict["duration"],
                        "dutch_name": translator.translate(duration_dict["english_name"], return_all=False)
                    }
                )
            except KeyError as ex:
                print(ex)
    with open("piles/pile_of_durations_dutch.csv", "w+", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["duration", "dutch_name"],
        )
        writer.writeheader()
        writer.writerows(pile_of_durations_dutch)


def translate_responses():
    print("Translating responses")
    pile_of_responses_dutch = list()

    with open("piles/pile_of_responses.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        pile_of_responses = list(reader)
        pile_of_responses = list(
            filter(
                lambda x: x["service"].split(".")[0] in SUPPORTED_DEVICES,
                pile_of_responses,
            )
        )
        for response_dict in progressbar(pile_of_responses):
            try:
                pile_of_responses_dutch.append(
                    {
                        "service": response_dict["service"],
                        "response": translate(response_dict["response"]),
                        "language": "nl",
                        "persona": response_dict["persona"],
                        "short": response_dict["short"],
                    }
                )
            except KeyError as ex:
                print(ex)
    with open("piles/pile_of_responses_dutch.csv", "w+", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["service", "response", "language", "persona", "short"]
        )
        writer.writeheader()
        writer.writerows(pile_of_responses_dutch)


def translate_system_prompts():
    print("Translating system prompts")
    pile_of_system_prompts_dutch = list()

    with open("piles/pile_of_system_prompts.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        pile_of_system_prompts = list(reader)
        for prompt_dict in progressbar(pile_of_system_prompts):
            try:
                pile_of_system_prompts_dutch.append(
                    {
                        "persona": prompt_dict["persona"],
                        "prompt": translate(prompt_dict["prompt"]),
                    }
                )
            except KeyError as ex:
                print(ex)
    with open("piles/pile_of_system_prompts_dutch.csv", "w+", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["persona", "prompt"]
        )
        writer.writeheader()
        writer.writerows(pile_of_system_prompts_dutch)

def translate_todo_items():
    print("Translating todo items")
    pile_of_todo_items_dutch = list()
    with open("piles/pile_of_todo_items.txt", encoding="utf-8") as f:
        english_phrases = f.readlines()
        for english_phrase in progressbar(english_phrases):
            pile_of_todo_items_dutch.append(f"{translator.translate(english_phrase, return_all=False)}\n")
    with open("piles/pile_of_todo_items_dutch.txt", "w+", encoding="utf-8") as f:
        f.writelines(pile_of_todo_items_dutch)

translate_device_names()
translate_templated_actions()
translate_specific_actions()
translate_status_requests()
translate_durations()
translate_responses()
translate_system_prompts()
translate_todo_items()