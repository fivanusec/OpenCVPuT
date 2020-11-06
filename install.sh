PS3='Select your linux flavor: '
options=("Ubuntu/Debian" "Arch" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Ubuntu/Debian")
            sudo apt install cmake
            break
            ;;
        "Arch")
            sudo pacman -S cmake
            break
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done

pip install cmake
pip install dlib
pip install numpy
pip install opencv-python
pip install face-recognition