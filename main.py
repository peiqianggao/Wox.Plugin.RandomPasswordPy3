# -*- coding: utf-8 -*-
import copy
import os
import random

import pyperclip
from wox import Wox

result_template = {
    'Title': '{}',
    'SubTitle': '+++ Click To Copy It +++',
    'IcoPath': 'password.png',
    'JsonRPCAction': {
        'method': 'copy_to_clipboard',
        'parameters': ['{}'],
    }
}

RANDOM_STR = "0123456789_AaBbCcDdEeFfGgHhIiJjKkLlMmNn0123456789OoPpQqRrSsTtUuVvWwXxYyZz0123456789"


class WoxRandomPasswordPy3(Wox):
    def query(self, query):
        results = list()
        num = 8
        if not query:
            length = 8
            num = 8
        else:
            keys = query.split()
            if len(keys) == 1 and keys[0].isdigit():
                length = int(keys[0])
            elif keys[0].isdigit() and keys[1].isdigit():
                length = int(keys[0])
                num = int(keys[1])
            else:
                length = 8
                num = 8

        for i in range(num):
            passwd = ''.join(random.sample(RANDOM_STR, length))
            res = copy.deepcopy(result_template)
            res['Title'] = res['Title'].format(passwd)
            res['JsonRPCAction']['parameters'][0] = res['JsonRPCAction']['parameters'][0].format(passwd)
            results.append(res)

        return results

    def copy_to_clipboard(self, value):
        """
        Copies the given value to the clipboard.
        WARNING:Uses yet-to-be-known Win32 API and ctypes black magic to work.
        """
        try:
            pyperclip.copy(value)
        except IOError:
            command = 'echo ' + value + '| clip'
            os.system(command)


if __name__ == "__main__":
    WoxRandomPasswordPy3()
