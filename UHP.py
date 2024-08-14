import random

class UHP:
    @staticmethod
    def UHP(file_path, double_safety): #Unicode Hashing Program
        with open(file_path, 'r') as file:
            f_read = file.read()
        words = f_read.split()

        if words:
            words[0] = chr(random.randint(32, 126))
            words[-1] = chr(random.randint(32, 126))

            for i in range(1, len(words) - 1):
                words[i] = chr(random.randint(32, 126))

        if double_safety:
            if words:
                words[0] = chr(random.randint(32, 126))
                words[-1] = chr(random.randint(32, 126))

                for i in range(1, len(words) - 1):
                    words[i] = chr(random.randint(32, 126))
        else:
            pass

        text = ' '.join(words)

        with open(file_path, 'w') as file:
            file.write(text)
