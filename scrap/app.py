from bs4 import BeautifulSoup


html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>My page</title>
</head>
<body>
    <div id="section-1">
        <h3 data-hello="hi">Hello</h3>
        <img src=""/>
        <p>Lorem ipsum dolor, sit amet consectetur adipiscing elit.</p>
    </div>
    <div id="section-2">
        <ul class="items">
            <li class="item"><a href="#">Item 1</a></li>
            <li class="item"><a href="#">Item 2</a></li>
            <li class="item"><a href="#">Item 3</a></li>
            <li class="item"><a href="#">Item 4</a></li>
            <li class="item"><a href="#">Item 5</a></li>
        </ul>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.head)
# print(soup.head.title)
# print(soup.body)

# el = soup.find_all('div')
# el = soup.find_all('div')[1]

# el = soup.find(id='section-1')
# el = soup.find(class_='items')
# el = soup.find(attrs={"data-hello":"hi"})

# el  = soup.select('#section-1')
# el  = soup.select('.item')[0]

# el = soup.find(class_='item').get_text()

# for item in soup.select('.item'):
#     print(item.get_text())

# el = soup.body.contents[1].contents[1].find_next_sibling()

# el = soup.find(id='section-2').find_previous_sibling()

# el = soup.find(class_='item').find_parent()

el = soup.find('h3').find_next_sibling('p')

print(el)