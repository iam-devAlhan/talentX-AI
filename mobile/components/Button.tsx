import { Pressable, View, Text, StyleSheet} from "react-native"

const Button = (props: any) => {

    return (
        <View style={styles.container}>
            <Pressable style={({pressed}) => [    
                    styles.button, {
                        backgroundColor: pressed ? "#02567F" : "#00aaff",    
                    }
                ]
            } onPress={() => console.log("Button Pressed!")}>
                <Text style={styles.text}>{props.children}</Text>
            </Pressable>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        padding: 20
    },
    button: {
        padding: 12,
        borderRadius: 10,
    },
    text: {
        color: "#fff",
        fontSize: 20,
        fontWeight: "bold"
    }
})
export default Button