START

    REPEAT
        DISPLAY menu
        READ choice

        IF choice is 5
            DISPLAY goodbye message
            EXIT loop
        END IF

        IF choice is not 1, 2, 3, or 4
            DISPLAY invalid choice message
            GO TO next iteration
        END IF

        READ first number
        READ second number

        IF choice is 1
            DISPLAY sum
        ELSE IF choice is 2
            DISPLAY difference
        ELSE IF choice is 3
            DISPLAY product
        ELSE IF choice is 4
            IF second number is zero
                DISPLAY division error
            ELSE
                DISPLAY quotient
            END IF
        END IF

    UNTIL user exits

STOP