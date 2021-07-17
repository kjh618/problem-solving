inp = input()
base_type, decls = inp.strip(';').split(' ', maxsplit=1)
decls = decls.split(', ')

for decl in decls:
    name = ''
    additional_type = ''
    for c in decl:
        if c == '*' or c == '&':
            additional_type = c + additional_type
        elif c == '[':
            additional_type = '[]' + additional_type
        elif c == ']':
            pass
        else:
            name += c

    print(f'{base_type}{additional_type} {name};')
