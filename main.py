class Automato:
  def __init__(self, states, initial_state, final_state, alphabet, transitions, input_symbols):
    self.states = states
    self.initial_state = initial_state
    self.final_state = final_state
    self.alphabet = alphabet
    self.current_state = initial_state
    self.input_symbols = input_symbols
  # def switch_over(self, state, symbol):

class State:
  def __init__(self, name, transitions, is_final = False, is_initial = False):
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
      '#states',
      '#initial',
      '#final',
      '#alphabet',
      '#transitions'
    ]
  def parse(self):
    formatted_input_symbols = self.format_input_symbols(self.input_symbols)
    for line in formatted_input_symbols:
      if line in self.reserved_words:
        print(f"Reserved: {line}")
      else:
        print(line)
    print(formatted_input_symbols)
  
  def format_input_symbols(self, input_symbols):
    return list(map(lambda word: word.strip(), input_symbols))

  def read_file(self, filename = 'input.txt'):
    with open(filename, 'r') as file:
      return file.readlines()


input_symbols = Parser().input_symbols

automato = Automato(
  states = [
    State(name = 's0', transitions = {'a':'s1', 'b':'s0'}, is_initial = True),
    State(name = 's1', transitions = {'a':'s1', 'b':'s0'}, is_final = True)
  ],
  initial_state = 's0',
  final_state = 's1',
  alphabet = ['a', 'b'],
  transitions = {
    's0': {'a':'s1', 'b':'s0'},
    's1': {'a':'s1', 'b':'s0'}
  },
  input_symbols = input_symbols
)

input_symbols = Parser().parse();
# print(automato.states)
# print(automato.input_symbols)