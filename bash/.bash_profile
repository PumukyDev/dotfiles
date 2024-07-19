#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

# PATH #
export PATH=$HOME/.local/bin:$HOME/.cargo/bin:$PATH

# Programs #
export TERM="kitty"
export NAVIGATOR="firefox"
export EDITOR="code"

# Clear temp directory #
[[ -d $HOME/tmp ]] && /bin/rm -rf $HOME/tmp/*
