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
         ('', '', 'towers2.krb'):
           [1649343150.175904, 'towers2_bc.py'],
         ('', '', 'towers_of_hanoi.krb'):
           [1649343150.1878886, 'towers_of_hanoi_bc.py'],
        },
        compiler_version)

