#import function to create app
from website import create_app

#initialize app
app = create_app()

#start server
if __name__ == '__main__':
    app.run(debug=True) 
