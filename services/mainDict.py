import sys
import os

from services.helperFunctions import *
from animations.InGameAnimations import *

game_plan = {
    '1': {
        'text': read_intro_file(os.path.abspath('textFiles/intro.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/intro.txt')),
                'animation': racing_track,
                'next': '2'
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/intro.txt')),
                'next': '5',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/intro.txt'))
            },
        },
    },
    '2': {

        'text': read_intro_file('textFiles/outro.txt'),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/outro.txt')),
                'next': '6',
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/outro.txt')),
                'next': '4',
            },
        },
    },
    '5': {
        'text': read_intro_file(os.path.abspath('textFiles/upgrade_avatar.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/upgrade_avatar.txt')),
                'animation': display_marketplace,
                'next': '7'
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/upgrade_avatar.txt')),
                'next': '9',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/upgrade_avatar.txt'))
            },
        },
    },
    '7': {
        'text': read_intro_file(os.path.abspath('textFiles/avatar_upgrade_backfire.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/avatar_upgrade_backfire.txt')),
                'animation': display_social_hub,
                'next': '9'
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/avatar_upgrade_backfire.txt')),
                'next': '9',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/avatar_upgrade_backfire.txt'))
            },
        },
    },
    '9': {
        'text': read_intro_file(os.path.abspath('textFiles/social_hub.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/social_hub.txt')),
                'next': '11'
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/social_hub.txt')),
                'next': '15',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/social_hub.txt'))
            },
        },
    },
    '11': {
        'text': read_intro_file(os.path.abspath('textFiles/mysterious_quest.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/mysterious_quest.txt')),
                'next': '13'
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/mysterious_quest.txt')),
                'next': '17',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/mysterious_quest.txt'))
            },
        },
    },
    '13': {
        'text': read_intro_file(os.path.abspath('textFiles/puzzle_completion.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/puzzle_completion.txt')),
                'next': '15'
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/puzzle_completion.txt')),
                'next': '15',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/puzzle_completion.txt'))
            },
        },
    },
    '15': {
        'text': read_intro_file(os.path.abspath('textFiles/mysterious_portal.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/mysterious_portal.txt')),
                'next': '25'
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/mysterious_portal.txt')),
                'next': '25',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/mysterious_portal.txt'))
            },
        },
    },
    '25': {
        'text': read_intro_file(os.path.abspath('textFiles/quest_continuation.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/quest_continuation.txt')),
                'next': '27'
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/quest_continuation.txt')),
                'next': '27',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/quest_continuation.txt'))
            },
        },
    },
    '27': {
        'text': read_intro_file(os.path.abspath('textFiles/ancient_virtual_city.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/ancient_virtual_city.txt')),
                'next': '23',
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/ancient_virtual_city.txt')),
                'next': '23',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/ancient_virtual_city.txt'))
            },
        },
    },
    '17': {
        'text': read_intro_file(os.path.abspath('textFiles/virtual_treasures.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/virtual_treasures.txt')),
                'next': '19',
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/virtual_treasures.txt')),
                'next': '19',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/virtual_treasures.txt'))
            },
        },
    },
    '19': {
        'text': read_intro_file(os.path.abspath('textFiles/epic_showdown.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/epic_showdown.txt')),
                'next': '21',
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/epic_showdown.txt')),
                'next': '21',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/epic_showdown.txt'))
            },
        },
    },
    '21': {
        'text': read_intro_file(os.path.abspath('textFiles/aftermath.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/aftermath.txt')),
                'next': '23',
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/aftermath.txt')),
                'next': '23',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/aftermath.txt'))
            },
        },
    },
    '23': {
        'text': read_intro_file(os.path.abspath('textFiles/virtual_legend.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/virtual_legend.txt')),
                'next': '23',
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/virtual_legend.txt')),
                'next': '2',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/virtual_legend.txt'))
            },
        },
    },
    '4': {
        'text': read_intro_file(os.path.abspath('textFiles/rival_revelation.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/rival_revelation.txt')),
                'next': '6',
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/rival_revelation.txt')),
                'next': '8',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/rival_revelation.txt'))
            },
        },
    },
    '6': {
        'text': read_intro_file(os.path.abspath('textFiles/intense_race.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/intense_race.txt')),
                'animation': find_shortcut,
                'next': '10',
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/intense_race.txt')),
                'next': '10',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/intense_race.txt'))
            },
        },
    },
    '10': {
        'text': read_intro_file(os.path.abspath('textFiles/shortcut_backfire.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/shortcut_backfire.txt')),
                'next': '14',
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/shortcut_backfire.txt')),
                'next': '14',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/shortcut_backfire.txt'))
            },
        },
    },
    '8': {
        'text': read_intro_file(os.path.abspath('textFiles/unexpected_ally.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/unexpected_ally.txt')),
                'next': '12',
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/unexpected_ally.txt')),
                'next': '10',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/unexpected_ally.txt'))
            },
        },
    },
    '12': {
        'text': read_intro_file(os.path.abspath('textFiles/unexpected_betrayal.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/unexpected_betrayal.txt')),
                'next': '14',
            },
            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/unexpected_betrayal.txt')),
                'next': '10',
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/unexpected_betrayal.txt'))
            },
        },
    },
    '14': {
        'text': read_intro_file(os.path.abspath('textFiles/alliance_formed.txt')),
        'options': {
            '1': {
                'text': extract_text_after_choice1(os.path.abspath('textFiles/alliance_formed.txt')),
                'animation': display_player_death_animation,
            },

            '2': {
                'text': extract_text_after_choice2(os.path.abspath('textFiles/alliance_formed.txt')),
                'animation': display_winning_animation
            },
            '3': {
                'text': extract_text_after_choice3(os.path.abspath('textFiles/alliance_formed.txt'))
            },
        },
    },
}

def execute_race_plan(race_plan):
    current_step = '1'

    while current_step is not None:
        step_info = race_plan[current_step]
        print(step_info['text'])

        options = step_info.get('options', {})
        if options:
            for key, value in options.items():
                print(f"{key} : {value['text']}")

            user_choice = input("\nEnter your choice: ")
            print()

            selected_option = options.get(user_choice, {})
            animation_function = selected_option.get('animation')

            if animation_function:
                # Run the animation function if present
                animation_function()

            next_step = selected_option.get('next')

            if user_choice == '3':
                print("Sad to see you leave :(")
                sys.exit()

            if next_step is not None:
                current_step = next_step
            else:
                print("Invalid choice. Exiting.")
                break
        else:
            print("End of the race plan.")
            break

# Execute the race plan
execute_race_plan(game_plan)
