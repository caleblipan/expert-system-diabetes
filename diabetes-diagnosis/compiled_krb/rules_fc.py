# rules_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def increased_thirst(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'increased_thirst', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'increased_thirst',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_increased_thirst(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'increased_thirst', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'increased_thirst',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def increased_hunger(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'increased_hunger', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'increased_hunger',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_increased_hunger(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'increased_hunger', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'increased_hunger',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def increased_urination(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'increased_urination', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'increased_urination',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_increased_urination(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'increased_urination', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'increased_urination',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def high_blood_sugar_risk_1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'increased_thirst', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'increased_hunger', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'blood_sugar_risk',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def high_blood_sugar_risk_2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'increased_thirst', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'increased_urination', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'blood_sugar_risk',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def high_blood_sugar_risk_3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'increased_hunger', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'increased_urination', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'blood_sugar_risk',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def low_blood_sugar_risk_1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'increased_thirst', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'increased_hunger', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'blood_sugar_risk',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def low_blood_sugar_risk_2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'increased_thirst', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'increased_urination', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'blood_sugar_risk',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def low_blood_sugar_risk_3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'increased_hunger', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'increased_urination', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'blood_sugar_risk',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def normal_glycemic_1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'blood_sugar_risk', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'blood_sugar',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def normal_glycemic_2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'blood_sugar_risk', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'high_glycemic', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'blood_sugar',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def hypoglycemic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'blood_sugar_risk', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'high_glycemic', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'blood_sugar',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def hyperglycemic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'blood_sugar_risk', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'high_glycemic', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'blood_sugar',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def diabetic_parent(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'diabetic_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'parent_is_diabetic',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def not_diabetic_parent(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'diabetic_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'parent_is_diabetic',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_diabetic_risk(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'blood_sugar_risk', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'blood_sugar', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'parent_is_diabetic', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('facts', 'is_diabetic',
                               (rule.pattern(0).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_diabetic_risk_with_diabetic_parent(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'blood_sugar_risk', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'blood_sugar', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'parent_is_diabetic', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('facts', 'is_diabetic',
                               (rule.pattern(0).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def low_diabetic_risk(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'blood_sugar_risk', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'blood_sugar', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'parent_is_diabetic', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('facts', 'is_diabetic',
                               (rule.pattern(0).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def very_low_diabetic_risk(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'blood_sugar_risk', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'blood_sugar', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'parent_is_diabetic', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('facts', 'is_diabetic',
                               (rule.pattern(0).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def very_high_diabetic_risk_high_glycemic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'blood_sugar', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'parent_is_diabetic', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'is_diabetic',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def high_diabetic_risk_high_glycemic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'blood_sugar', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'parent_is_diabetic', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'is_diabetic',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def very_high_diabetic_risk_low_glycemic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'blood_sugar', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'parent_is_diabetic', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'is_diabetic',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def high_diabetic_risk_low_glycemic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'blood_sugar', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'parent_is_diabetic', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'is_diabetic',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  fc_rule.fc_rule('increased_thirst', This_rule_base, increased_thirst,
    (('questions', 'increased_thirst',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_increased_thirst', This_rule_base, no_increased_thirst,
    (('questions', 'increased_thirst',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('increased_hunger', This_rule_base, increased_hunger,
    (('questions', 'increased_hunger',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_increased_hunger', This_rule_base, no_increased_hunger,
    (('questions', 'increased_hunger',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('increased_urination', This_rule_base, increased_urination,
    (('questions', 'increased_urination',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_increased_urination', This_rule_base, no_increased_urination,
    (('questions', 'increased_urination',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('high_blood_sugar_risk_1', This_rule_base, high_blood_sugar_risk_1,
    (('facts', 'increased_thirst',
      (pattern.pattern_literal(True),),
      False),
     ('facts', 'increased_hunger',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal('high'),))
  
  fc_rule.fc_rule('high_blood_sugar_risk_2', This_rule_base, high_blood_sugar_risk_2,
    (('facts', 'increased_thirst',
      (pattern.pattern_literal(True),),
      False),
     ('facts', 'increased_urination',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal('high'),))
  
  fc_rule.fc_rule('high_blood_sugar_risk_3', This_rule_base, high_blood_sugar_risk_3,
    (('facts', 'increased_hunger',
      (pattern.pattern_literal(True),),
      False),
     ('facts', 'increased_urination',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal('high'),))
  
  fc_rule.fc_rule('low_blood_sugar_risk_1', This_rule_base, low_blood_sugar_risk_1,
    (('facts', 'increased_thirst',
      (pattern.pattern_literal(False),),
      False),
     ('facts', 'increased_hunger',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal('low'),))
  
  fc_rule.fc_rule('low_blood_sugar_risk_2', This_rule_base, low_blood_sugar_risk_2,
    (('facts', 'increased_thirst',
      (pattern.pattern_literal(False),),
      False),
     ('facts', 'increased_urination',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal('low'),))
  
  fc_rule.fc_rule('low_blood_sugar_risk_3', This_rule_base, low_blood_sugar_risk_3,
    (('facts', 'increased_hunger',
      (pattern.pattern_literal(False),),
      False),
     ('facts', 'increased_urination',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal('low'),))
  
  fc_rule.fc_rule('normal_glycemic_1', This_rule_base, normal_glycemic_1,
    (('facts', 'blood_sugar_risk',
      (pattern.pattern_literal('low'),),
      False),),
    (pattern.pattern_literal('normal'),))
  
  fc_rule.fc_rule('normal_glycemic_2', This_rule_base, normal_glycemic_2,
    (('facts', 'blood_sugar_risk',
      (pattern.pattern_literal('high'),),
      False),
     ('questions', 'high_glycemic',
      (pattern.pattern_literal('normal'),),
      False),),
    (pattern.pattern_literal('normal'),))
  
  fc_rule.fc_rule('hypoglycemic', This_rule_base, hypoglycemic,
    (('facts', 'blood_sugar_risk',
      (pattern.pattern_literal('high'),),
      False),
     ('questions', 'high_glycemic',
      (pattern.pattern_literal('low'),),
      False),),
    (pattern.pattern_literal('low'),))
  
  fc_rule.fc_rule('hyperglycemic', This_rule_base, hyperglycemic,
    (('facts', 'blood_sugar_risk',
      (pattern.pattern_literal('high'),),
      False),
     ('questions', 'high_glycemic',
      (pattern.pattern_literal('high'),),
      False),),
    (pattern.pattern_literal('high'),))
  
  fc_rule.fc_rule('diabetic_parent', This_rule_base, diabetic_parent,
    (('questions', 'diabetic_parent',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('not_diabetic_parent', This_rule_base, not_diabetic_parent,
    (('questions', 'diabetic_parent',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('no_diabetic_risk', This_rule_base, no_diabetic_risk,
    (('facts', 'blood_sugar_risk',
      (pattern.pattern_literal('low'),),
      False),
     ('facts', 'blood_sugar',
      (pattern.pattern_literal('normal'),),
      False),
     ('facts', 'parent_is_diabetic',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal("No need for a blood glucose test. You should be fine."),))
  
  fc_rule.fc_rule('no_diabetic_risk_with_diabetic_parent', This_rule_base, no_diabetic_risk_with_diabetic_parent,
    (('facts', 'blood_sugar_risk',
      (pattern.pattern_literal('low'),),
      False),
     ('facts', 'blood_sugar',
      (pattern.pattern_literal('normal'),),
      False),
     ('facts', 'parent_is_diabetic',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("No need for a blood glucose test. You should be fine.\nBe careful though. Your parents is diabetic."),))
  
  fc_rule.fc_rule('low_diabetic_risk', This_rule_base, low_diabetic_risk,
    (('facts', 'blood_sugar_risk',
      (pattern.pattern_literal('high'),),
      False),
     ('facts', 'blood_sugar',
      (pattern.pattern_literal('normal'),),
      False),
     ('facts', 'parent_is_diabetic',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Your risk of diabetes is low"),))
  
  fc_rule.fc_rule('very_low_diabetic_risk', This_rule_base, very_low_diabetic_risk,
    (('facts', 'blood_sugar_risk',
      (pattern.pattern_literal('high'),),
      False),
     ('facts', 'blood_sugar',
      (pattern.pattern_literal('normal'),),
      False),
     ('facts', 'parent_is_diabetic',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal("Your risk of diabetes is very low"),))
  
  fc_rule.fc_rule('very_high_diabetic_risk_high_glycemic', This_rule_base, very_high_diabetic_risk_high_glycemic,
    (('facts', 'blood_sugar',
      (pattern.pattern_literal('high'),),
      False),
     ('facts', 'parent_is_diabetic',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Your risk of diabetes is very high!"),))
  
  fc_rule.fc_rule('high_diabetic_risk_high_glycemic', This_rule_base, high_diabetic_risk_high_glycemic,
    (('facts', 'blood_sugar',
      (pattern.pattern_literal('high'),),
      False),
     ('facts', 'parent_is_diabetic',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal("Your risk of diabetes is high"),))
  
  fc_rule.fc_rule('very_high_diabetic_risk_low_glycemic', This_rule_base, very_high_diabetic_risk_low_glycemic,
    (('facts', 'blood_sugar',
      (pattern.pattern_literal('low'),),
      False),
     ('facts', 'parent_is_diabetic',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Your risk of diabetes is very high!"),))
  
  fc_rule.fc_rule('high_diabetic_risk_low_glycemic', This_rule_base, high_diabetic_risk_low_glycemic,
    (('facts', 'blood_sugar',
      (pattern.pattern_literal('low'),),
      False),
     ('facts', 'parent_is_diabetic',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal("Your risk of diabetes is high"),))


Krb_filename = '..\\rules.krb'
Krb_lineno_map = (
    ((12, 16), (4, 4)),
    ((17, 18), (6, 6)),
    ((27, 31), (10, 10)),
    ((32, 33), (12, 12)),
    ((42, 46), (16, 16)),
    ((47, 48), (18, 18)),
    ((57, 61), (22, 22)),
    ((62, 63), (24, 24)),
    ((72, 76), (28, 28)),
    ((77, 78), (30, 30)),
    ((87, 91), (34, 34)),
    ((92, 93), (36, 36)),
    ((102, 106), (43, 43)),
    ((107, 111), (44, 44)),
    ((112, 113), (46, 46)),
    ((122, 126), (50, 50)),
    ((127, 131), (51, 51)),
    ((132, 133), (53, 53)),
    ((142, 146), (57, 57)),
    ((147, 151), (58, 58)),
    ((152, 153), (60, 60)),
    ((162, 166), (64, 64)),
    ((167, 171), (65, 65)),
    ((172, 173), (67, 67)),
    ((182, 186), (71, 71)),
    ((187, 191), (72, 72)),
    ((192, 193), (74, 74)),
    ((202, 206), (78, 78)),
    ((207, 211), (79, 79)),
    ((212, 213), (81, 81)),
    ((222, 226), (88, 88)),
    ((227, 228), (90, 90)),
    ((237, 241), (94, 94)),
    ((242, 246), (95, 95)),
    ((247, 248), (97, 97)),
    ((257, 261), (101, 101)),
    ((262, 266), (102, 102)),
    ((267, 268), (104, 104)),
    ((277, 281), (108, 108)),
    ((282, 286), (109, 109)),
    ((287, 288), (111, 111)),
    ((297, 301), (116, 116)),
    ((302, 303), (118, 118)),
    ((312, 316), (122, 122)),
    ((317, 318), (124, 124)),
    ((327, 331), (130, 130)),
    ((332, 336), (131, 131)),
    ((337, 341), (132, 132)),
    ((342, 343), (134, 134)),
    ((352, 356), (137, 137)),
    ((357, 361), (138, 138)),
    ((362, 366), (139, 139)),
    ((367, 368), (141, 141)),
    ((377, 381), (146, 146)),
    ((382, 386), (147, 147)),
    ((387, 391), (148, 148)),
    ((392, 393), (150, 150)),
    ((402, 406), (154, 154)),
    ((407, 411), (155, 155)),
    ((412, 416), (156, 156)),
    ((417, 418), (158, 158)),
    ((427, 431), (163, 163)),
    ((432, 436), (164, 164)),
    ((437, 438), (166, 166)),
    ((447, 451), (171, 171)),
    ((452, 456), (172, 172)),
    ((457, 458), (174, 174)),
    ((467, 471), (179, 179)),
    ((472, 476), (180, 180)),
    ((477, 478), (182, 182)),
    ((487, 491), (186, 186)),
    ((492, 496), (187, 187)),
    ((497, 498), (189, 189)),
)
