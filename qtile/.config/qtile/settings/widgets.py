

programas = {
        'firefox': 'firefox',
        'terminal': 'alacritty',
        'editor': 'code',
        'thunar': 'thunar',
        'steam':'steam',
        'tor':'Tor Browser',
        'a':'a',
        'b':'b',
        'c':'c',
        'd':'d',
        'e':'e',
        'f':'f',
        'g':'g',
        'h':'h',
        'i':'i',
        'j':'j',
        'k':'k',
    }

sex={
    'steam':'steam',
        'tor':'Tor Browser',
        'a':'a',
        'b':'b',
        'c':'c',
        'd':'d',
        'e':'e',
        'f':'f',
        'g':'g',
        'h':'h',
        'i':'i',
        'j':'j',
        'k':'k',
}



def show_program_menu(qtile, program_list):
    menu_options = "\n".join(program_list.keys())
    rofi_command = "rofi -theme+window+width 18% -dmenu -p 'Selecciona un programa' -lines {0} -location 1 -yoffset 46".format(len(program_list))
    rofi_process = subprocess.Popen(rofi_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    selected_program = rofi_process.communicate(input=menu_options.encode())[0].decode().strip()
    if selected_program in program_list:
        programa_path = program_list[selected_program]
        qtile.cmd_spawn(programa_path)
        
        
        

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)



