from thonny import get_workbench
from thonny.workbench import SyntaxThemeSettings


def dracula() -> SyntaxThemeSettings:
    '''
    Dracula Theme v1.2.5

    Copyright 2017, All rights reserved

    Code licensed under the MIT license
    http://zenorocha.mit-license.org

    @author Zeno Rocha <hi@zenorocha.com>

    -- Thonny Version by github.com/danspinola <dspinola.dev@gmail.com>
    
    References:
    https://github.com/dracula/dracula-theme
    https://spec.draculatheme.com/
    '''
    
    # THEME COLOUR SCHEME
    # Standard/Base
    BG = '#282A36'
    FG = '#F8F8F2'
    CURLINE = '#44475a'
    SELECTION = '#44475A'
    COMMENT = '#6272A4'
    RED = '#FF5555'
    ORANGE = '#FFB86C'
    YELLOW = '#F1FA8C'
    GREEN = '#50FA7B'
    PURPLE = '#BD93F9'
    CYAN = '#8BE9FD'
    PINK = '#FF79C6'
    # Extras
    WHITE = '#F8F8F2'
    BLACK = '#21222C'
    BGDARKER = '#191A21'
    BGLIGHT = '#343746'
    BGLIGHTER = '#424450'
    COMMENTLIGHTER = '#7F94D4'
    # Fonts - Editor (Thonny)
    NORMAL = "EditorFont"
    BOLD = "BoldEditorFont"
    ITALICS = "ItalicEditorFont"
    BOLDIT = "BoldItalicEditorFont"
    # Fonts - Shell IO (Thonny)
    NORMAL_IO = "IOFont"
    BOLD_IO = "BoldIOFont"
    ITALICS_IO = "ItalicIOFont"
    BOLDIT_IO = "BoldItalicIOFont"

    return {
        # EDITOR
        "TEXT":{
            "foreground": FG,
            "insertbackground": FG,
            "background": BG,
            },
        "GUTTER":{ # line numbers <<
            "foreground": COMMENT,
            "background": BG
            },
        "breakpoint": {
            "foreground": PINK
            },
        "current_line": {
            "background": CURLINE,
            },
        "sel": { # selection
            "foreground": PINK,
            "background": SELECTION
            },
        "definition": {
            "foreground": GREEN,
            "font": BOLD
            },
        "string": { # editor
            "foreground": YELLOW
            },
        "string3": { # shell
            "foreground": YELLOW,
            "background": None,
            "font": NORMAL
            },
        "open_string": { # editor
            "foreground": YELLOW, 
            "background": SELECTION
            },
        "open_string3": { # shell
            "foreground": YELLOW,
            "background": SELECTION,
            "font": NORMAL,
            },
        "builtin": {
            "foreground": CYAN,
            "font": BOLD
            },
        "keyword": {
            "foreground": PINK,
            "font": BOLD
            },
        "number": {
            "foreground": PURPLE
            },
        "comment": {
            "foreground": COMMENT
            },
        "welcome": { 
            "foreground": PINK
            },
        "magic": {
            "foreground": PURPLE
            },
        # SHELL
        "prompt": {
            "foreground": CYAN,
            "font": BOLD
            },
        "stdin": {
            "foreground": WHITE
            },
        "stdout": {
            "foreground": FG
            },
        "stderr": {
            "foreground": RED
            },
        "value": {
            "foreground": YELLOW
            },
        "hyperlink": {
            "foreground": CYAN,
            "underline": False,
            "font": BOLD_IO
            },
        # PAREN MATCHER
        "surrounding_parens": {
            "foreground": ORANGE,
            "font": BOLD
            },
        "unclosed_expression": {
            "background": BGDARKER
            },
        # FIND/REPLACE
        "found": {
            "underline": False,
            "foreground": WHITE,
            "background": RED,
            "font": BOLD
            },
        "current_found": {
            "foreground": BLACK,
            "background": ORANGE,
            "font": BOLD
            }, 
        "local_name": { # variables
            "foreground": FG,
            "font": NORMAL
            },
        # DEBUGGER
        "active_focus": {
            "background": BGLIGHTER,
            "borderwidth": 1,
            "relief": "solid"
            },
        "suspended_focus": {
            "background": BGDARKER,
            "borderwidth": 1,
            "relief": "solid"
            },
        "completed_focus": {
            "background": BGLIGHTER,
            "borderwidth": 1,
            "relief": "flat"
            },
        "exception_focus": {
            "foreground": BLACK,
            "background": PINK,
            "borderwidth": 1,
            "relief": "solid"
            },
        "expression_box": {
            "background": BGLIGHT,
            "foreground": FG
            },
    }

def load_plugin():
    get_workbench().add_syntax_theme("Dracula", "Default Dark", dracula)