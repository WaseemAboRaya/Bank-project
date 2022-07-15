import xml.etree.ElementTree as ET

tree = ET.parse('stam.xml')
root = tree.getroot()
print(root)

for country in root.findall('country'):
    print(country.get('name'))
    print(country.find('rank').text)
    print(country.find('year').text)
    print(country.find('gdppc').text)
