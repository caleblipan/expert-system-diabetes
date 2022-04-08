# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'facts.kfb'):
           [1649404173.9150324, 'facts.fbc'],
         ('', '', 'questions.kqb'):
           [1649404173.9187627, 'questions.qbc'],
         ('', '', 'rules.krb'):
           [1649404173.9337544, 'rules_fc.py'],
        },
        compiler_version)

