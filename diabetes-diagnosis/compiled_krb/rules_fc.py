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

def increased_fatigue(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'increased_fatigue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'increased_fatigue',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_increased_fatigue(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'increased_fatigue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'increased_fatigue',
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
             else engine.lookup('facts', 'increased_thirst', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'increased_fatigue', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'blood_sugar_risk',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def high_blood_sugar_risk_4(rule, context = None, index = None):
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

def high_blood_sugar_risk_5(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'increased_hunger', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'increased_fatigue', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'blood_sugar_risk',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def high_blood_sugar_risk_6(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'increased_urination', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'increased_fatigue', context,
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
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'increased_urination', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
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
                 else engine.lookup('facts', 'increased_hunger', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'increased_fatigue', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
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
             else engine.lookup('facts', 'increased_thirst', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'increased_urination', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'increased_fatigue', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('facts', 'blood_sugar_risk',
                               (rule.pattern(0).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def low_blood_sugar_risk_4(rule, context = None, index = None):
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
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'increased_fatigue', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
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
                 else engine.lookup('questions', 'random_glucose_test', context,
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
                 else engine.lookup('questions', 'random_glucose_test', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'blood_sugar',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def higher_than_normal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'blood_sugar_risk', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'random_glucose_test', context,
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
                 else engine.lookup('questions', 'random_glucose_test', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'blood_sugar',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def confirmed_diabetic(rule, context = None, index = None):
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
            engine.assert_('facts', 'is_diabetic',
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
  
  fc_rule.fc_rule('increased_fatigue', This_rule_base, increased_fatigue,
    (('questions', 'increased_fatigue',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_increased_fatigue', This_rule_base, no_increased_fatigue,
    (('questions', 'increased_fatigue',
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
    (('facts', 'increased_thirst',
      (pattern.pattern_literal(True),),
      False),
     ('facts', 'increased_fatigue',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal('high'),))
  
  fc_rule.fc_rule('high_blood_sugar_risk_4', This_rule_base, high_blood_sugar_risk_4,
    (('facts', 'increased_hunger',
      (pattern.pattern_literal(True),),
      False),
     ('facts', 'increased_urination',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal('high'),))
  
  fc_rule.fc_rule('high_blood_sugar_risk_5', This_rule_base, high_blood_sugar_risk_5,
    (('facts', 'increased_hunger',
      (pattern.pattern_literal(True),),
      False),
     ('facts', 'increased_fatigue',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal('high'),))
  
  fc_rule.fc_rule('high_blood_sugar_risk_6', This_rule_base, high_blood_sugar_risk_6,
    (('facts', 'increased_urination',
      (pattern.pattern_literal(True),),
      False),
     ('facts', 'increased_fatigue',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal('high'),))
  
  fc_rule.fc_rule('low_blood_sugar_risk_1', This_rule_base, low_blood_sugar_risk_1,
    (('facts', 'increased_thirst',
      (pattern.pattern_literal(False),),
      False),
     ('facts', 'increased_hunger',
      (pattern.pattern_literal(False),),
      False),
     ('facts', 'increased_urination',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal('low'),))
  
  fc_rule.fc_rule('low_blood_sugar_risk_2', This_rule_base, low_blood_sugar_risk_2,
    (('facts', 'increased_thirst',
      (pattern.pattern_literal(False),),
      False),
     ('facts', 'increased_hunger',
      (pattern.pattern_literal(False),),
      False),
     ('facts', 'increased_fatigue',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal('low'),))
  
  fc_rule.fc_rule('low_blood_sugar_risk_3', This_rule_base, low_blood_sugar_risk_3,
    (('facts', 'increased_thirst',
      (pattern.pattern_literal(False),),
      False),
     ('facts', 'increased_urination',
      (pattern.pattern_literal(False),),
      False),
     ('facts', 'increased_fatigue',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal('low'),))
  
  fc_rule.fc_rule('low_blood_sugar_risk_4', This_rule_base, low_blood_sugar_risk_4,
    (('facts', 'increased_hunger',
      (pattern.pattern_literal(False),),
      False),
     ('facts', 'increased_urination',
      (pattern.pattern_literal(False),),
      False),
     ('facts', 'increased_fatigue',
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
     ('questions', 'random_glucose_test',
      (pattern.pattern_literal('normal'),),
      False),),
    (pattern.pattern_literal('normal'),))
  
  fc_rule.fc_rule('hypoglycemic', This_rule_base, hypoglycemic,
    (('facts', 'blood_sugar_risk',
      (pattern.pattern_literal('high'),),
      False),
     ('questions', 'random_glucose_test',
      (pattern.pattern_literal('low'),),
      False),),
    (pattern.pattern_literal('low'),))
  
  fc_rule.fc_rule('higher_than_normal', This_rule_base, higher_than_normal,
    (('facts', 'blood_sugar_risk',
      (pattern.pattern_literal('high'),),
      False),
     ('questions', 'random_glucose_test',
      (pattern.pattern_literal('high'),),
      False),),
    (pattern.pattern_literal('high'),))
  
  fc_rule.fc_rule('hyperglycemic', This_rule_base, hyperglycemic,
    (('facts', 'blood_sugar_risk',
      (pattern.pattern_literal('high'),),
      False),
     ('questions', 'random_glucose_test',
      (pattern.pattern_literal('veryHigh'),),
      False),),
    (pattern.pattern_literal('veryHigh'),))
  
  fc_rule.fc_rule('confirmed_diabetic', This_rule_base, confirmed_diabetic,
    (('facts', 'blood_sugar_risk',
      (pattern.pattern_literal('high'),),
      False),
     ('facts', 'blood_sugar',
      (pattern.pattern_literal('veryHigh'),),
      False),),
    (pattern.pattern_literal("Confirmed. You have diabetes.\nWe will give you insulin injections immediately."),))
  
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
    (pattern.pattern_literal("No need for a blood glucose test. You should be fine.\nBe careful though. One of your parents is diabetic."),))
  
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
    (pattern.pattern_literal("Looks like your blood sugar level is OK, despite the symptoms you have shown.\nYour risk of diabetes is low.\nBe careful though. One of your parents is diabetic."),))
  
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
    (pattern.pattern_literal("Your risk of diabetes is very low, despite the symptoms you have shown.\nYour blood sugar level is normal and none of your parents is diabetic."),))
  
  fc_rule.fc_rule('very_high_diabetic_risk_high_glycemic', This_rule_base, very_high_diabetic_risk_high_glycemic,
    (('facts', 'blood_sugar',
      (pattern.pattern_literal('high'),),
      False),
     ('facts', 'parent_is_diabetic',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("I'm sorry, but you currently have prediabetes.\nYour risk of diabetes is very high!"),))
  
  fc_rule.fc_rule('high_diabetic_risk_high_glycemic', This_rule_base, high_diabetic_risk_high_glycemic,
    (('facts', 'blood_sugar',
      (pattern.pattern_literal('high'),),
      False),
     ('facts', 'parent_is_diabetic',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal("I'm sorry, but you currently have prediabetes.\nYour risk of diabetes is high"),))
  
  fc_rule.fc_rule('very_high_diabetic_risk_low_glycemic', This_rule_base, very_high_diabetic_risk_low_glycemic,
    (('facts', 'blood_sugar',
      (pattern.pattern_literal('low'),),
      False),
     ('facts', 'parent_is_diabetic',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("I'm sorry, but you currently have prediabetes.\nYour risk of diabetes is very high!"),))
  
  fc_rule.fc_rule('high_diabetic_risk_low_glycemic', This_rule_base, high_diabetic_risk_low_glycemic,
    (('facts', 'blood_sugar',
      (pattern.pattern_literal('low'),),
      False),
     ('facts', 'parent_is_diabetic',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal("I'm sorry, but you currently have prediabetes.\nYour risk of diabetes is high"),))


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
    ((102, 106), (40, 40)),
    ((107, 108), (42, 42)),
    ((117, 121), (46, 46)),
    ((122, 123), (48, 48)),
    ((132, 136), (55, 55)),
    ((137, 141), (56, 56)),
    ((142, 143), (58, 58)),
    ((152, 156), (62, 62)),
    ((157, 161), (63, 63)),
    ((162, 163), (65, 65)),
    ((172, 176), (69, 69)),
    ((177, 181), (70, 70)),
    ((182, 183), (72, 72)),
    ((192, 196), (76, 76)),
    ((197, 201), (77, 77)),
    ((202, 203), (79, 79)),
    ((212, 216), (83, 83)),
    ((217, 221), (84, 84)),
    ((222, 223), (86, 86)),
    ((232, 236), (90, 90)),
    ((237, 241), (91, 91)),
    ((242, 243), (93, 93)),
    ((252, 256), (97, 97)),
    ((257, 261), (98, 98)),
    ((262, 266), (99, 99)),
    ((267, 268), (101, 101)),
    ((277, 281), (105, 105)),
    ((282, 286), (106, 106)),
    ((287, 291), (107, 107)),
    ((292, 293), (109, 109)),
    ((302, 306), (113, 113)),
    ((307, 311), (114, 114)),
    ((312, 316), (115, 115)),
    ((317, 318), (117, 117)),
    ((327, 331), (121, 121)),
    ((332, 336), (122, 122)),
    ((337, 341), (123, 123)),
    ((342, 343), (125, 125)),
    ((352, 356), (132, 132)),
    ((357, 358), (134, 134)),
    ((367, 371), (138, 138)),
    ((372, 376), (139, 139)),
    ((377, 378), (141, 141)),
    ((387, 391), (145, 145)),
    ((392, 396), (146, 146)),
    ((397, 398), (148, 148)),
    ((407, 411), (152, 152)),
    ((412, 416), (153, 153)),
    ((417, 418), (155, 155)),
    ((427, 431), (159, 159)),
    ((432, 436), (160, 160)),
    ((437, 438), (162, 162)),
    ((447, 451), (167, 167)),
    ((452, 456), (168, 168)),
    ((457, 458), (170, 170)),
    ((467, 471), (175, 175)),
    ((472, 473), (177, 177)),
    ((482, 486), (181, 181)),
    ((487, 488), (183, 183)),
    ((497, 501), (189, 189)),
    ((502, 506), (190, 190)),
    ((507, 511), (191, 191)),
    ((512, 513), (193, 193)),
    ((522, 526), (197, 197)),
    ((527, 531), (198, 198)),
    ((532, 536), (199, 199)),
    ((537, 538), (201, 201)),
    ((547, 551), (206, 206)),
    ((552, 556), (207, 207)),
    ((557, 561), (208, 208)),
    ((562, 563), (210, 210)),
    ((572, 576), (214, 214)),
    ((577, 581), (215, 215)),
    ((582, 586), (216, 216)),
    ((587, 588), (218, 218)),
    ((597, 601), (223, 223)),
    ((602, 606), (224, 224)),
    ((607, 608), (226, 226)),
    ((617, 621), (231, 231)),
    ((622, 626), (232, 232)),
    ((627, 628), (234, 234)),
    ((637, 641), (239, 239)),
    ((642, 646), (240, 240)),
    ((647, 648), (242, 242)),
    ((657, 661), (246, 246)),
    ((662, 666), (247, 247)),
    ((667, 668), (249, 249)),
)
