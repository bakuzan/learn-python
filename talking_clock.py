import collections

Words = collections.namedtuple('Words', ['h', 'm', 'oh', 'am_pm'])

inputs = [
    "00:00",
    "01:30",
    "12:05",
    "14:01",
    "20:29",
    "21:00"
]

word_map = {
    '00': '',
    '01': 'one',
    '02': 'two',
    '03': 'three',
    '04': 'four',
    '05': 'five',
    '06': 'six',
    '07': 'seven',
    '08': 'eight',
    '09': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'tweleve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty'
}

def find_word_parts(s):
    a,b = list(s)
    x = a.ljust(2, '0')
    y = b.rjust(2, '0')
    x_str = word_map[x] if x in word_map else ''
    y_str = word_map[y] if y in word_map else ''
    return "{0} {1}".format(x_str, y_str)

def time_in_words(time):
    h, m = time.split(":")
    oh = ' oh' if str.startswith(m, '0') and m != '00' else ''
    am_pm = ' pm' if int(h) > 11 else ' am'
    h = h if int(h) < 13 else str(int(h) - 12).rjust(2, '0')
    h_str = word_map[h] if h in word_map else find_word_parts(h)
    m_str = word_map[m] if m in word_map else find_word_parts(m)
    h_str = h_str if h_str else word_map["12"]
    m_str = m_str if not m_str else " {}".format(m_str)
    return Words(h_str, m_str, oh, am_pm)


for t in inputs:
    print("It's {0}{2}{1}{3}".format(*time_in_words(t)))