#!/usr/bin/env bash
### Colored read line

function my_read(){

    RED='\033[0;31m'
    NC='\033[0m' # No Color
		 RESET=`tput sgr0` # reset all colors

    echo -e "${RED}"
    read -n $1 -p "$2 "
    echo -e "${RESET}"

}

### yesno first variant

function yesno(){
    echo "Do you wish to continue? yes/no"
    select yn in "yes" "no"; do
        case ${yn} in
            yes ) return 0;;
            no ) return 1;;
            * ) echo "Please answer yes or no (use 1 or 2)";;
        esac
    done
}

### yesno second variant

function yesno2(){
    echo "Do you wish to continue? yes/no"
    select yn in "yes" "no"; do
        case ${yn} in
            yes ) break;;
            no ) exit;;
            * ) echo "Please answer yes or no.";;
        esac
    done

}


### yesno third variant

function yesno3(){
	while true; do
	    read -p "Do you wish to install this program?" yn
	    case $yn in
	        [Yy]* ) break;;
	        [Nn]* ) exit;;
	        * ) echo "Please answer yes or no.";;
	    esac
	done
}

function cecho(){
    RED='\033[0;31m'
    NC='\033[0m' # No Color
    echo -e "\n${RED}$1${NC}\n";

}

function my_read(){

    RED='\033[0;31m'
    NC='\033[0m' # No Color

    echo -e "${RED}"
    read -n $1 -p "$2 "
    echo -e "${NC}"

}
