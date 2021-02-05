PS3='Select your linux flavor: '
options=("Ubuntu/Debian" "Arch" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Ubuntu/Debian")
            sudo apt install cmake
            pip3 install cmake
            pip3 install dlib
            pip3 install numpy
            pip3 install opencv-python
            pip3 install face-recognition
            break
            ;;
        "Arch")
            sudo pacman -S cmake
            pip install cmake
            pip install dlib
            pip install numpy
            pip install opencv-python
            pip install face-recognition
            break
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
