import os.path
import sys
from unittest import TestCase

from racko import main
from tud_test_base import *

def test_racko():
    try:
        exist = os.path.exists("racko.py")
        assert exist == True
    except:
        sys.exit()

    set_keyboard_input(['y','4','5','p','1','60','0','-5','12','29','p','57','p','23','d','p','27','p','27','48'])
    main()
    output = get_display_output()
    assert output == [
        "----- Welcome to Rack - O! -----",
        "Enter y to display instructions: ",
        "The goal of the game is to get the cards in your rack of cards",
        "into ascending order. Your rack has ten slots numbered 1 to 10.",
        "During your turn you can draw the top card of the deck or take",
        "the top card of the discard pile.",
        "If you draw the top card of the deck, you can use that card to",
        "replace a card in one slot of your rack. The replaced card goes to",
        "the discard pile.",
        "Alternatively you can simply choose to discard the drawn card.",
        "If you take the top card of the discard pile you must use it to",
        "replace a card in one slot of your rack. The replaced card goes",
        "to the top of the discard pile.",
        "Enter number for initial seed: ",
        "Enter the size of the rack to use. Must be between 5 and 10: ",
        "",
        "Player 1's turn.",
        "Your current rack  [29, 48, 46, 50, 23]",
        "Top of discard pile  1",
        "Enter d to draw anything else to take top of discard pile: ",
        "",
        "Enter the card number to replace with the 1: ",
        "1 is not in your rack.",
        "Enter the card number to replace with the 1: ",
        "60 is not in your rack.",
        "Enter the card number to replace with the 1: ",
        "0 is not in your rack.",
        "Enter the card number to replace with the 1: ",
        "-5 is not in your rack.",
        "Enter the card number to replace with the 1: ",
        "12 is not in your rack.",
        "Enter the card number to replace with the 1: ",
        "The rack after the turn  [1, 48, 46, 50, 23]",
        "",
        "Player 2's turn.",
        "Your current rack  [40, 44, 57, 55, 27]",
        "Top of discard pile  29",
        "Enter d to draw anything else to take top of discard pile: ",
        "",
        "Enter the card number to replace with the 29: ",
        "The rack after the turn  [40, 44, 29, 55, 27]",
        "",
        "Player 1's turn.",
        "Your current rack  [1, 48, 46, 50, 23]",
        "Top of discard pile  57",
        "Enter d to draw anything else to take top of discard pile: ",
        "",
        "Enter the card number to replace with the 57: ",
        "The rack after the turn  [1, 48, 46, 50, 57]",
        "",
        "Player 2's turn.",
        "Your current rack  [40, 44, 29, 55, 27]",
        "Top of discard pile  23",
        "Enter d to draw anything else to take top of discard pile: ",
        "",
        "drew the 52",
        "Enter p to place card, anything else to discard it: ",
        "Enter the card number to replace with the 52: ",
        "The rack after the turn  [40, 44, 29, 55, 52]",
        "",
        "Player 1's turn.",
        "Your current rack  [1, 48, 46, 50, 57]",
        "Top of discard pile  27",
        "Enter d to draw anything else to take top of discard pile: ",
        "",
        "Enter the card number to replace with the 27: ",
        "27 is not in your rack."
        "Enter the card number to replace with the 27: ",
        "The rack after the turn  [1, 27, 46, 50, 57]",
        "",
        "Player 1 wins!"
    ]