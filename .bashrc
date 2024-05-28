### EXPORT ###
export EDITOR='vim'
export VISUAL='vim'
export HISTCONTROL=ignoreboth:erasedups
export PAGER='most'
export PATH="$HOME/.config/emacs/bin:$HOME/.local/bin:$HOME/.config/composer/vendor/bin:/mnt/glados/Programming/Go/bin:$HOME/.local/share/npm-global/bin:$PATH"

# PS1='[\u@\h \W]\$ '
PS1="\[\e[38;5;33m\]\u\[\e[38;5;69m\]@\[\e[38;5;105m\]\h \[\e[38;5;141m\]\w \[\033[0m\]$ "

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

#ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

### ALIASES ###
alias ls='exa'
alias l='exa'
alias ll='exa -l --icons'
alias la='exa --icons -ld .*'
alias grep='rg'
alias cp="cp -i"     # confirm before overwriting something
alias df='df -h'     # human-readable sizes
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
alias mine-zeph='sudo /mnt/pi/mining/run/arch/zeph.sh'
alias mine-mecu='sudo /mnt/pi/mining/run/arch/mecu.sh'
alias mine-rtc='sudo /mnt/pi/mining/run/arch/rtc.sh'
alias mine-gprx='sudo /mnt/pi/mining/run/arch/gprx.sh'
alias mine-mo='sudo /mnt/pi/mining/run/arch/mocean-alt.sh'
alias hss='hugo server --noHTTPCache'
alias rg="rg -g '!{**/node_modules/*,**/.git/*,**/target/*}' --hidden --follow"
#grub update
alias update-grub="sudo grub-mkconfig -o /boot/grub/grub.cfg"
alias grub-update="sudo grub-mkconfig -o /boot/grub/grub.cfg"
#grub issue 08/2022
alias install-grub-efi="sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=ArcoLinux"
#check vulnerabilities microcode
alias microcode='grep . /sys/devices/system/cpu/vulnerabilities/*'
#gpg
#verify signature for isos
alias gpg-check="gpg2 --keyserver-options auto-key-retrieve --verify"
alias fix-gpg-check="gpg2 --keyserver-options auto-key-retrieve --verify"
#receive the key of a developer
alias gpg-retrieve="gpg2 --keyserver-options auto-key-retrieve --receive-keys"
alias fix-gpg-retrieve="gpg2 --keyserver-options auto-key-retrieve --receive-keys"
alias fix-keyserver="[ -d ~/.gnupg ] || mkdir ~/.gnupg ; cp /etc/pacman.d/gnupg/gpg.conf ~/.gnupg/ ; echo 'done'"

fastfetch
