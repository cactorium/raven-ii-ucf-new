## *********************************************************
## 
## File autogenerated for the raven_2 package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 233, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 259, 'description': 'An offet to add to the shoulder_l', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'shoulder_l', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -50.0, 'type': 'double'}, {'srcline': 259, 'description': 'An offet to add to the elbow_l', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'elbow_l', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -50.0, 'type': 'double'}, {'srcline': 259, 'description': 'An offet to add to the insertion_l', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'insertion_l', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -50.0, 'type': 'double'}, {'srcline': 259, 'description': 'An offet to add to the roll_l', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'roll_l', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -50.0, 'type': 'double'}, {'srcline': 259, 'description': 'An offet to add to the wrist_l', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'wrist_l', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -50.0, 'type': 'double'}, {'srcline': 259, 'description': 'An offet to add to the grasp1_l', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'grasp1_l', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -50.0, 'type': 'double'}, {'srcline': 259, 'description': 'An offet to add to the grasp2_l', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'grasp2_l', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -50.0, 'type': 'double'}, {'srcline': 259, 'description': 'An offet to add to the shoulder_r', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'shoulder_r', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -50.0, 'type': 'double'}, {'srcline': 259, 'description': 'An offet to add to the elbow_r', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'elbow_r', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -50.0, 'type': 'double'}, {'srcline': 259, 'description': 'An offet to add to the shoulder_r', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'insertion_r', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -50.0, 'type': 'double'}, {'srcline': 259, 'description': 'An offet to add to the roll_r', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'roll_r', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -50.0, 'type': 'double'}, {'srcline': 259, 'description': 'An offet to add to the wrist_r', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'wrist_r', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -50.0, 'type': 'double'}, {'srcline': 259, 'description': 'An offet to add to the grasp1_r', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'grasp1_r', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -50.0, 'type': 'double'}, {'srcline': 259, 'description': 'An offet to add to the grasp2_r', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'grasp2_r', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -50.0, 'type': 'double'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

