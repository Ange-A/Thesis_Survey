from otree.api import*


class C(BaseConstants):
    NAME_IN_URL = 'fashion_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Title = models.StringField(
        label="Please select your title?",
        choices=[
            ['Mr.', 'Mr.'],
            ['Mrs.', 'Mrs.'],
            ['Ms.', 'Ms.']],

        widget=widgets.RadioSelect,
    )

    Age = models.IntegerField(
        label="Please enter your age:",
        min=18,
        max=100,
    )

    Preferences = models.StringField(
        choices=[["Never", "Never"],
                 ["Sometimes", "Sometimes"],
                 ["Often", "Often"],
                 ["Frequently", "Frequently"]],

        label="How often do you buy fast fashion items",

        widget=widgets.RadioSelect,
    )

    Income = models.StringField(
        label="Please select your monthly income range",
        choices=[
            ["$0-$500", "$0-$500"],
            ["$500 - $1000", "$500 - $1000"],
            ["$1500 - $3000", "$1500 - $3000"],
            ["$3000 - $5000", "$3000 - $5000"],
            ["$6000+", "$6000+"]],

        widget=widgets.RadioSelect,
    )

    Definition = models.StringField(
        choices=[["Quick made garments", "Quick made garments"],
                 ["Affordable garments", "Affordable garments"],
                 ["Trendy garments", "Trendy garments"],
                 ["Both", "Both"],
                 ["I have no idea", "I have no idea"]],

        label="How would you describe fast fashion",

        widget=widgets.RadioSelect,
    )

    Sustainable = models.StringField(
        choices=[["Never", "Never"],
                 ["Sometimes", "Sometimes"],
                 ["Often", "Often"],
                 ["Frequently", "Frequently"]],

        label="Do you think fast fashion brands practice sustainability",

        widget=widgets.RadioSelect,
    )

    Brands = models.StringField(
        choices=[["Never", "Never"],
                 ["Sometimes", "Sometimes"],
                 ["Often", "Often"],
                 ["Frequently", "Frequently"]],
        label="Do you think brands that call themselves sustainable are actually sustainable",

        widget=widgets.RadioSelect,
    )

    Budget = models.StringField(
        choices=[["Never", "Never"],
                 ["Sometimes", "Sometimes"],
                 ["Often", "Often"],
                 ["Frequently", "Frequently"]],

        label="With consideration of your budget, would you spend an "
               "extra 5 dollars to buy a sustainably manufactured fashion item?",

        widget=widgets.RadioSelect,
    )

    Rate = models.StringField(
        choices=[["Yes", "Yes"],
                 ["No", "No"]],

        label="On a rate of 1 to 5, how did the previous"
              " video influence your orientation towards sustainable fast fashion items.",

        widget=widgets.RadioSelect,
    )

    Likely = models.StringField(
        choices=[["Yes", "Yes"],
                 ["No", "No"]],

        label="With consideration of your budget, would you spend an "
              "extra 5 dollars to buy a sustainably manufactured fashion item?",

        widget=widgets.RadioSelect,

    )

    Actually = models.StringField(
        choices=[["Never", "Never"],
                 ["Sometimes", "Sometimes"],
                 ["Often", "Often"],
                 ["Frequently", "Frequently"]],

        label="Do you think brands that call themselves sustainable are  actually sustainable",

        widget=widgets.RadioSelect,
    )

    condition = models.IntegerField()


def creating_session(subsession):
    import itertools
    clist = itertools.cycle([0, 1])
    for player in subsession.get_players():
        player.condition = next(clist)


class Demographics(Page):
    form_model = 'player'
    form_fields = ['Title', 'Age', 'Preferences', 'Income', 'Definition']


class Sustainability(Page):
    form_model = 'player'
    form_fields = ['Sustainable', 'Brands', 'Budget']


class Intervention0(Page):
    def is_displayed(player: Player):
        return player.condition == 0

    form_model = 'player'


class Intervention1(Page):
    def is_displayed(player: Player):
        return player.condition == 1

    form_model = 'player'


class Final(Page):
    form_model = 'player'
    form_fields = ['Rate', 'Likely', 'Actually']


page_sequence = [Demographics, Sustainability, Intervention0, Intervention1, Final]
