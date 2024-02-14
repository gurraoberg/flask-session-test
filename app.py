from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def handle_data():
    data = {
        "cats": [
            {
                "name": "sille"
            },
            {
                "name": "monri"
            }
        ]
    }

    cat_list = []
    for cat in data['cats']:
        cat_list.append(cat['name'])
    return cat_list

@app.route('/add-many-cats')
def add_many_cats():

    cat_list = session.get('cat_list') # Get sessions old cat list
    details_page = session.get('details_page')

    for i in range(1, 51): # Add 50 cats
        cat = f"Mjau{i}"
        cat_list.append(cat)

    num_cats = len(cat_list)
    print(num_cats)
    session['num_cats'] = num_cats # Set sessions total cats
    session['cat_list'] = cat_list # Set sessions new cat list
    return render_template('index.html',
                           cat_list=cat_list,
                           details_page=details_page,
                           num_cats=num_cats)

@app.route('/add-cat')
def add_cat():

    cat_list = session.get('cat_list') # Get sessions old cat list
    
    details_page = session.get('details_page')
    if len(cat_list) % 2:
        new = "sille"
    else:
        new = "monri"
    cat_list.append(new)
    num_cats = len(cat_list)
    session['num_cats'] = num_cats # Set sessions total cats
    session['cat_list'] = cat_list # Set sessions new cat list


    return render_template('index.html',
                           cat_list=cat_list,
                           details_page=details_page,
                           num_cats=num_cats)
    

@app.route('/remove-cat')
def details():
    
    cat_list = session.get('cat_list')
    num_cats = session.get('num_cats') # Get current amount of cats

    if len(cat_list) > 0:
        cat_list.pop(0)
    if len(cat_list) == 0:
        error = "Error no cats left."
        return render_template('index.html',
                               error=error)
    
    details_page = True
    session['details_page'] = details_page # Set details page to true
    num_cats = len(cat_list) # Set new amount of cats
    session['num_cats'] = num_cats # Set sessions new amount of cats
    return render_template('index.html',
                           cat_list=cat_list,
                           details_page=details_page,
                           num_cats=num_cats)

@app.route('/')
def index():
    
    session.clear() # if '/' is called clear session.

    cat_list = handle_data()
    session['cat_list'] = cat_list

    return render_template('index.html',
                           cat_list=cat_list)

if __name__ == '__main__':
    app.run(debug=True)
