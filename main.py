import requests

def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]

def main():
    url = 'https://www.amcharts.com/lib/3/maps/svg/'
    file = open('Countries.txt', 'r')

    countries = []
    line = file.readline()
    while line != '':
        countries.append(camelCase(line.lower()))
        line = file.readline()

    for country in countries:
        print(country)
        country = country + 'Low'
        countryUrl = country + '.svg'
        imgUrl: str = url + countryUrl
        image = requests.get(imgUrl)
        open('countries_svg/' + countryUrl, 'wb').write(image.content)


if __name__ == '__main__':
    main()