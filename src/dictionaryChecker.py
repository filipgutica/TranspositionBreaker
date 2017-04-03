#
# Example of checking for english words using pyenchant library.
#
#you must run 'pip install pyenchant' first
import enchant


d = enchant.Dict("en_US")
tempText = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the ' \
           'industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and ' \
           'scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into ' \
           'electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release ' \
           'of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software ' \
           'like Aldus PageMaker including versions of Lorem Ipsum.'

def main(argv):
    data = argv.split(' ')
    counter = 0
    for word in data:
        if d.check(word):
            counter += 1
    print('Potential Words: ' + str(len(data)) + ' Real Words: ' + str(counter) + ' Percentage: ' + str((counter/len(data))))
    return [len(data), counter, (counter/len(data))]

if __name__ == '__main__':
    x = main(tempText)
    print(x)
