class Automato:

    def __init__(self, states, initial_state, final_state, alphabet,
                 transitions):
        self.states = states
        self.initial_state = initial_state
        self.final_state = final_state
        self.alphabet = alphabet
        self.current_state = initial_state


class State:

    def __init__(self, name, transitions, is_final=False, is_initial=False):
        self.name = name
        self.transitions = transitions
        self.is_final = is_final
        self.is_initial = is_initial

    def __repr__(self):
        return self.name


class Parser:

    def __init__(self):
        self.match = "ˆ(s\d):(\w)>(s\d)$"
        self.input_symbols = self.read_file()
        self.reserved_words = [
            '#states', '#initial', '#accepting', '#alphabet', '#transitions'
        ]

    def parse(self):
        formatted_input_symbols = self.format_input_symbols(self.input_symbols)
        statesRange = formatted_input_symbols.index(self.reserved_words[0])
        initialRange = formatted_input_symbols.index(self.reserved_words[1])
        acceptingRange = formatted_input_symbols.index(self.reserved_words[2])
        alphabetRange = formatted_input_symbols.index(self.reserved_words[3])
        transitionsRange = formatted_input_symbols.index(
            self.reserved_words[4])

        # Remove last item from formatted_input_symbols

        states = formatted_input_symbols[statesRange + 1:initialRange]
        initial_state = formatted_input_symbols[initialRange +
                                                1:acceptingRange]
        accepting_state = formatted_input_symbols[acceptingRange +
                                                  1:alphabetRange]
        alphabet = formatted_input_symbols[alphabetRange + 1:transitionsRange]
        transitions = formatted_input_symbols[transitionsRange + 1:]

        print(
            f"""States: {states}\nInitial: {initial_state}\nAccepting: {accepting_state}\nAlphabet: {alphabet}\nTransitions: {transitions}"""
        )

        # Get the string from the file and convert to the state class
        formattedStates = []
        for state in states:
            formattedTransitions = []
            is_initial = True if state in initial_state else False
            is_final = True if state in accepting_state else False
            for transition in transitions:
                transitionSplit = transition.split(':')
                if transitionSplit[0] == state:
                    [alphabetWord, stateToGo] = transitionSplit[1].split('>')
                    formattedTransitions.append({alphabetWord: stateToGo})
            s = State(name=state,
                      transitions=formattedTransitions,
                      is_initial=is_initial,
                      is_final=is_final)
            formattedStates.append(s)

        automato = Automato(states=formattedStates,
                            initial_state=initial_state,
                            final_state=accepting_state,
                            alphabet=alphabet,
                            transitions=transitions)

        return automato

    def format_input_symbols(self, input_symbols):
        return list(map(lambda word: word.strip(), input_symbols))

    def read_file(self, filename='input.txt'):
        try:
            with open(filename, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f'{filename} was not found')
            exit()


automato = Parser().parse()

# automato = Automato(
#   states = [
#     State(name = 's0', transitions = {'a':'s1', 'b':'s0'}, is_initial = True),
#     State(name = 's1', transitions = {'a':'s1', 'b':'s0'}, is_final = True)
#   ],
#   initial_state = 's0',
#   final_state = 's1',
#   alphabet = ['a', 'b'],
#   transitions = {
#     's0': {'a':'s1', 'b':'s0'},
#     's1': {'a':'s1', 'b':'s0'}
#   },
#   input_symbols = input_symbols
# )

# input_symbols = Parser().parse();
# print(automato.states)
# print(automato.input_symbols)
