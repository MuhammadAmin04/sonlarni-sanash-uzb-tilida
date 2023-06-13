# istalgan sonni o'zbek tilida o'qib beradigan dastur
class NumWord:
    def __init__(self, n1 = int):
        self.n1 = n1
        self.birlik = {
            1: ' bir ', 2: ' ikki ', 3: ' uch ', 4: ' tort ', 5: ' besh ',
            6: ' olti ', 7: ' yetti ', 8: ' sakkiz ', 9: ' toqqiz ', 
        }
        self.onlik = {
            1: ' o\'n ', 2: ' yigirma ', 3: ' ottiz ', 4: ' qirq ', 5: ' ellik ',
            6: ' oltmish ', 7: ' yetmish ', 8: ' sakson ', 9: ' toqson ', 
        }
        self.sad = {
            1: '', 2: ' ming ', 3: ' million ',
            4: ' milliard ', 5: ' trilion ', 6: ' septilion '
        }

    def num(self):
        a = self.n1
        massive = []
        while a:
            massive.append(a % 1000)
            a //= 1000
        return massive[::-1]

    def __str__(self):
        str1 = ''
        array = self.num()
        if self.n1 != 0:
            length = len(array)
            for i in array:
                x1 = i // 100
                x2 = i // 10 % 10
                x3 = i % 10
                if not x1 == 0:
                    str1 += self.birlik[x1] + 'yuz'
                if not x2 == 0:
                    str1 += self.onlik[x2] + ' '
                if not x3 == 0:
                    str1 += self.birlik[x3]
                if not length == 0:
                    str1 += self.sad[length]
                length -= 1
        else: 
            str1 = 'nol'
        return str1.replace('  ',' ')
    
n = int(input('Enter N: '))
object = NumWord(n)
print(object)