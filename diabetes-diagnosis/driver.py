import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal

engine = knowledge_engine.engine(__file__)

def start_diagnosis():

    engine.reset()

    engine.activate('rules')
 
    try:
        with engine.prove_goal('facts.is_diabetic($result)') as gen:
            for vars, plan in gen:
                print("\n%s" % (vars['result']))

    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)

    print()
