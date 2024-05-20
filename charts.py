import matplotlib.pyplot as plt
import pandas as pd

def main(name):
    category_data = {
        'categ_id': [17, 19, 1, 8, 4, 11, 16, 15, 12, 10, 2, 20, 18],
        'name': ['ground', 'street', 'oil', 'drug', 'source', 'drive', 'return', 'news', 'goal', 'shoulder', 'rich',
                 'lose', 'loss'],
        'book_count': [4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    }

    author_data = {
        'author_id': [39, 67, 28, 60, 34, 16, 73, 42, 15, 48, 26, 57, 61, 77, 25, 3, 20, 33, 1, 64, 71, 8, 80, 35, 31,
                      22, 65],
        'name': ['Wanda Holmes', 'Amanda Larsen', 'Samantha Moore', 'Summer Peters', 'Mary Hayes', 'Julia Gonzalez',
                 'Anna Rodriguez', 'Emily Duncan', 'Julie Leach', 'Sierra Rosales', 'Brent Jones', 'Edward Huff',
                 'Michael Jones', 'Kristin Johnson', 'Maria Gordon', 'Kyle Cantu', 'Jaclyn Adams', 'Melissa Gonzalez',
                 'Marisa Bell', 'Tina Davis', 'Antonio Delacruz', 'Jessica Obrien', 'Spencer Baldwin', 'Thomas Clayton',
                 'Christina Smith', 'Heather Nguyen', 'Deborah Taylor'],
        'book_count': [3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    }

    category_df = pd.DataFrame(category_data)
    author_df = pd.DataFrame(author_data)

    def create_pie_chart(df, column, title):
        plt.figure(figsize=(8, 8))
        plt.pie(df[column], labels=df['name'], autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.axis('equal')
        plt.show()

    def create_bar_chart(df, column, title):
        plt.figure(figsize=(10, 8))
        plt.bar(df['name'], df[column], color='skyblue')
        plt.xlabel('Authors')
        plt.ylabel('Book Count')
        plt.title(title)
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    create_pie_chart(category_df, 'book_count', 'Количество книг в каждой категории')

    create_bar_chart(author_df, 'book_count', 'Количество книг каждого автора')


if __name__ == '__main__':
    main()