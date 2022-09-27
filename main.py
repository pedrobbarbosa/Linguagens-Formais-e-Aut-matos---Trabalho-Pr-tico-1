class Automato:

    def __init__(self, states, final_state, alphabet, transitions):
        self.states = states
        self.initial_state = [
            state if state.is_initial else None for state in states
        ]
        self.final_state = [
            state if state.is_final else None for state in states
        ]
        self.alphabet = alphabet
        self.current_state = self.initial_state[0]
        self.transitions = transitions
        self.accepting_state = final_state

    def transition(self, symbol):
        if symbol in self.alphabet:
            for transition in self.current_state.transitions:
                if symbol in transition:
                    for state in self.states:
                        if state.name == transition.get(symbol):
                            self.current_state = state
                            return True
        else:
            raise Exception("Symbol not in alphabet")

    def __repr__(self):
        return (
            f"""Estados: {self.states}\nEstado Inicial: {self.initial_state}\nEstado de aceitação: {self.accepting_state}\nAlfabeto: {self.alphabet}\nTransições: {self.transitions}"""
        )


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

        automato = Automato(
            states=formattedStates,
            # initial_state=initial_state,
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
print(automato)

entry_point = input("\nDigite uma palavra: ")

for symbol in entry_point:
    automato.transition(symbol)

print(f"\n Estado atual após as transições: {automato.current_state}")
