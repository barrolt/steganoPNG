from itertools import cycle
from typing import List, Union

import numpy as np

class Vigenere():
    def __init__(self, key):
        self.key = key
        self.auto_key = False
        self.base = 0


    def _int_encrypt_(self, list_int_plain_text: List[int], key_now: str) -> str:
        list_int_key = self.str_to_list_int(key_now, base=self.base)

        if (self.auto_key):
            list_int_key += list_int_plain_text

        list_int_cipher_text = [
            (num + key) % 256
            for key, num in zip(cycle(list_int_key), list_int_plain_text)
        ]

        return list_int_cipher_text

    def _int_decrypt_(self, list_int_cipher_text: List[int], key_now: str) -> str:
        list_int_key = self.str_to_list_int(key_now, base=self.base)
        if self.auto_key:
            if key_now == '':
                return ''

            list_int_plain_text = []
            for idx, num in enumerate(list_int_cipher_text):
                key = list_int_key[idx]
                plain_int = (num - key) % 256
                list_int_plain_text.append(plain_int)
                list_int_key.append(plain_int)
        else:
            list_int_plain_text = [(num - key) % 256 for key, num in zip(
                cycle(list_int_key), list_int_cipher_text)]

        return list_int_plain_text

    def encryptFile(self, fileName):
        if fileName:
            # if outputFile:
                # fileSize = os.stat(fileName).st_size
                # nLoop = ceil(fileSize / OFFSET)
                binary = np.fromfile(fileName, dtype=np.uint8)
                print(binary)
                cipher_list_int = self._int_encrypt_(binary, self.key)
                print(cipher_list_int)
                arr = np.asarray(cipher_list_int, dtype=np.uint8)
                print(arr)
                # arr.tofile(outputFile)
                # print('done encrypt')
                return arr.tobytes()

    def decryptFile(self, fileName, outputFile):
        if fileName:
            if outputFile:
                # fileSize = os.stat(fileName).st_size
                # nLoop = ceil(fileSize / OFFSET)
                binary = np.fromfile(fileName, dtype=np.uint8)
                print(binary)
                plain_list_int = self._int_decrypt_(binary, self.key)
                print(plain_list_int)
                arr = np.asarray(plain_list_int, dtype=np.uint8)
                print(arr)
                arr.tofile(outputFile)
                # print('done decrypt')
                # return arr.tobytes()

    @staticmethod
    def str_to_list_int(
        text: Union[str, List[str]], base: int = ord('a')) -> List[int]:
        '''Convert str to list of int
        Convertion done by substract each char by base,
        so the smallest char will have int = 0
        '''
        print([(ord(char) - base) for char in text])

        return [(ord(char) - base) for char in text]


