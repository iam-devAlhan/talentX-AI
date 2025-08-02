import { View, Text, TextInput } from "react-native"
import Button from "@/components/Button"
import styled from "styled-components/native"

const Container = styled.View`
    flex: 1;
    background-color: #1c1c1c;
    justify-content: flex-start;
    align-items: flex-start;
`

const Header = styled.Text`
    color: white;
    padding: 5%;
    font-size: 30px;
    font-weight: 800;
`

const Input = styled.TextInput`
    padding: 10px;
`
export default function Login() {
    return (
        <>
            <Container>
                <Header>Login Screen</Header>
                <Button>Hello World</Button>
            </Container>
        </>
    )
}