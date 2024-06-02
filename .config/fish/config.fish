

set -U fish_greeting ""


# PATHS
export PATH="$HOME/.config/emacs/bin:$HOME/.local/bin:$HOME/.cargo/bin:$HOME/.config/composer/vendor/bin:/mnt/glados/Programming/Go/bin:$HOME/.local/share/npm-global/bin:$PATH"
export GOPATH=/mnt/glados/Programming/Go
export GOBIN=/mnt/glados/Programming/Go/bin


if status is-interactive
    alias ls='exa'
    alias l='exa'
    alias ll='exa -l --icons'
    alias la='exa --icons -ld .*'
    alias grep='rg'
    alias cp="cp -i" # confirm before overwriting something
    alias df='df -h' # human-readable sizes
    alias free='free -m' # show sizes in MB
    alias cat='bat'
    alias tree='exa -la --tree --icons'
    alias tre='exa -a --tree --icons'
    alias userlist="cut -d: -f1 /etc/passwd | sort"
    alias sizeof="du -sh"
    alias shuty='sudo shutdown now'
    alias iftop='sudo iftop | lolcat'
    alias radeontop='sudo radeontop -c'
    alias v='nvim'
    alias aspell='aspell -c -t'
    alias :q='exit'
    alias logout='pkill -KILL -u $USER'
    alias :w='cowsay -d "A specter is haunting the modern world"'
    alias mine-nh='sudo /mnt/pi/mining/run/arch/nicehash.sh'
    alias mine-mo='sudo /mnt/pi/mining/run/arch/mocean-alt.sh'
    alias mine-xmr-alt='sudo /mnt/pi/mining/run/arch/xmr-alt.sh'
    alias mine-xmr='sudo /mnt/pi/mining/run/arch/xmr.sh'
    alias hss='hugo server --noHTTPCache'
    alias rg="rg -g '!{**/node_modules/*,**/.git/*,**/target/*}' --hidden --follow"
end

# neofetch
fastfetch
