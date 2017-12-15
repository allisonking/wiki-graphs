from app import wikigraph

@wikigraph.route('/')
@wikigraph.route('/index')
def index():
    return 'Welcome!'
