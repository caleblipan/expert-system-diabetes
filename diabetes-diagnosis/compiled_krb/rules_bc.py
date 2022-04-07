# rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def hypoglycemic(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'high_glycemic', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.hypoglycemic: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def hyperglycemic(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'high_glycemic', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.hyperglycemic: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def diabetic_parent(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'diabetic_parent', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.diabetic_parent: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def not_diabetic_parent(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'diabetic_parent', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.not_diabetic_parent: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def very_high_diabetic_risk(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'blood_sugar', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.very_high_diabetic_risk: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'parent_is_diabetic', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.very_high_diabetic_risk: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def high_diabetic_risk(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'blood_sugar', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.high_diabetic_risk: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'parent_is_diabetic', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.high_diabetic_risk: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def low_diabetic_risk(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'blood_sugar', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.low_diabetic_risk: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'parent_is_diabetic', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.low_diabetic_risk: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def very_low_diabetic_risk(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'blood_sugar', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.very_low_diabetic_risk: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'parent_is_diabetic', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.very_low_diabetic_risk: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  bc_rule.bc_rule('hypoglycemic', This_rule_base, 'blood_sugar',
                  hypoglycemic, None,
                  (pattern.pattern_literal('low'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('hyperglycemic', This_rule_base, 'blood_sugar',
                  hyperglycemic, None,
                  (pattern.pattern_literal('high'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('diabetic_parent', This_rule_base, 'parent_is_diabetic',
                  diabetic_parent, None,
                  (pattern.pattern_literal(True),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('not_diabetic_parent', This_rule_base, 'parent_is_diabetic',
                  not_diabetic_parent, None,
                  (pattern.pattern_literal(False),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('very_high_diabetic_risk', This_rule_base, 'is_diabetic',
                  very_high_diabetic_risk, None,
                  (pattern.pattern_literal("Your risk of diabetes is very high!"),),
                  (),
                  (pattern.pattern_literal('high'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('high_diabetic_risk', This_rule_base, 'is_diabetic',
                  high_diabetic_risk, None,
                  (pattern.pattern_literal("Your risk of diabetes is high!"),),
                  (),
                  (pattern.pattern_literal('high'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('low_diabetic_risk', This_rule_base, 'is_diabetic',
                  low_diabetic_risk, None,
                  (pattern.pattern_literal("Your risk of diabetes is low"),),
                  (),
                  (pattern.pattern_literal('low'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('very_low_diabetic_risk', This_rule_base, 'is_diabetic',
                  very_low_diabetic_risk, None,
                  (pattern.pattern_literal("Your risk of diabetes is very low"),),
                  (),
                  (pattern.pattern_literal('low'),
                   pattern.pattern_literal(False),))


Krb_filename = '..\\rules.krb'
Krb_lineno_map = (
    ((14, 18), (3, 3)),
    ((20, 25), (5, 5)),
    ((38, 42), (8, 8)),
    ((44, 49), (10, 10)),
    ((62, 66), (14, 14)),
    ((68, 73), (16, 16)),
    ((86, 90), (19, 19)),
    ((92, 97), (21, 21)),
    ((110, 114), (25, 25)),
    ((116, 121), (27, 27)),
    ((122, 127), (28, 28)),
    ((140, 144), (31, 31)),
    ((146, 151), (33, 33)),
    ((152, 157), (34, 34)),
    ((170, 174), (37, 37)),
    ((176, 181), (39, 39)),
    ((182, 187), (40, 40)),
    ((200, 204), (43, 43)),
    ((206, 211), (45, 45)),
    ((212, 217), (46, 46)),
)
