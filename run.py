import re
data = 'Mo    08:00-20:00'

print(re.search('\w{2}', data).group())

pattern = re.compile(r'([01]?[0-9]|2[0-3]):[0-5][0-9]')

print([match.group() for match in pattern.finditer(re.sub('[a-zA-Z\s]', '', data))])

print([match.group() for match in re.finditer('([01]?[0-9]|2[0-3]):[0-5][0-9]', re.sub('[a-zA-Z\s]', '', data))])

days = {
    'Mo': 'Monday',
    'Di': 'Tuesday',
    'Mi': 'Wednesday',
    'do': 'Thursday',
    'Fr': 'Friday',
    'Sat.': 'Saturday',
    'So': 'Sunday'
}