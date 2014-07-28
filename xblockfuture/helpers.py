from xblock.fields import Scope, Integer, String

# This should be a field type? 
class Grade():
    def __init__(self, maxgrade = 1):
        self._maxgrade = maxgrade
        self._grade = None

    def __get__(self):
        logging.warn("This is really rather unsupported!")
        return None  # self.grade

    def __set__(self, grade):
        self.parent.runtime.publish(self, 'grade', {'value':grade, 'max_value': self._maxgrade})
        self._grade = grade

    def set_parent(self, parent):
        self.parent = parent

    def get_maxscore(self):
        return self._maxscore

def future(original_class, config={}):
    ''' Modify the class c to support future proposed features. 
    '''
    # Step 1: Give it a useful name. 

    if 'name' in config:
        class_name = config['name']
    elif hasattr(original_class, 'display_name'):
        class_name = original_class.display_name
    elif hasattr(original_class, 'name'):
        class_name = original_class.name
    else:
        class_name = str(type(original_class))
    original_class.display_name = String(default=class_name, 
                                         scope=Scope.settings,
                                         help="Display name")

    # Step 2: Manage grading
    if hasattr(original_class, grade) and isinstance(grade, Grade):
        original_class.has_score = True
        original_class.max_score = lambda x: return x.grade.get_maxscore()

    return original_class
