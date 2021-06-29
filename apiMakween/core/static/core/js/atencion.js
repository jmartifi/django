$(document).ready(function(){
    
    $('#id_tbat_fch_ingreso').get(0).type = 'date';
    
    $('#formRegistrar').submit(function(e){
        var form = valForReg();
        if(form == 1){
            e.preventDefault();
        }
    });  
    $('#id_tbus_dsc_nombre').focusout(function(){
        if($(this).val().length == 0){
            $(this).css('border', '2px solid #dc3545');
            $(this).css('background-color', '#f8d7da');
        }else{
            $(this).css('border', '2px solid #155724');
            $(this).css('background-color', '#d4edda');
        }
    });    
    $('#id_tbus_dsc_apellido').focusout(function(){
        if($(this).val().length == 0){
            $(this).css('border', '2px solid #dc3545');
            $(this).css('background-color', '#f8d7da');
        }else{
            $(this).css('border', '2px solid #155724');
            $(this).css('background-color', '#d4edda');
        }
    });    
    $('#id_tbus_dsc_email').focusout(function(){
        if($(this).val().length == 0){
            $(this).css('border', '2px solid #dc3545');
            $(this).css('background-color', '#f8d7da');
        }else{
            $(this).css('border', '2px solid #155724');
            $(this).css('background-color', '#d4edda');
        }
    });
    $('#id_tbus_dsc_pass').focusout(function(){
        if($(this).val().length == 0){
            $(this).css('border', '2px solid #dc3545');
            $(this).css('background-color', '#f8d7da');
        }else{
            $(this).css('border', '2px solid #155724');
            $(this).css('background-color', '#d4edda');
        }
    });
});

function valForReg(){
    V_err = 0;
    V_txtErr = '<b>Hay error(es):</b><br><br>';
    if($('#id_tbus_dsc_nombre').val().length == 0){
        $('#id_tbus_dsc_nombre').css('border', '2px solid #dc3545');
        $('#id_tbus_dsc_nombre').css('background-color', '#f8d7da');
        V_err++;
        V_txtErr += 'Nombre no puede ser vacío.<br>';
    }else{
        $('#id_tbus_dsc_nombre').css('border', '2px solid #155724');
        $('#id_tbus_dsc_nombre').css('background-color', '#d4edda');
    }
    if($('#id_tbus_dsc_apellido').val().length == 0){
        $('#id_tbus_dsc_apellido').css('border', '2px solid #dc3545');
        $('#id_tbus_dsc_apellido').css('background-color', '#f8d7da');
        V_err++;
        V_txtErr += 'Apellido no puede ser vacío.<br>';
    }else{
        $('#id_tbus_dsc_apellido').css('border', '2px solid #155724');
        $('#id_tbus_dsc_apellido').css('background-color', '#d4edda');
    }
    if($('#id_tbus_dsc_email').val().length == 0){
        $('#id_tbus_dsc_email').css('border', '2px solid #dc3545');
        $('#id_tbus_dsc_email').css('background-color', '#f8d7da');
        V_err++;
        V_txtErr += 'Correo electrónico no puede ser vacío.<br>';
    }else{
        if($("#id_tbus_dsc_email").val().indexOf('@', 0) == -1 || $("#id_tbus_dsc_email").val().indexOf('.', 0) == -1) {
            $('#id_tbus_dsc_email').css('border', '2px solid #dc3545');
            $('#id_tbus_dsc_email').css('background-color', '#f8d7da');
            V_err++;
            V_txtErr += 'Correo electrónico no es valida.<br>';
        }else{
            $('#id_tbus_dsc_email').css('border', '2px solid #155724');
            $('#id_tbus_dsc_email').css('background-color', '#d4edda');
        }
    }
    if($('#id_tbus_dsc_pass').val().length == 0){
        $('#id_tbus_dsc_pass').css('border', '2px solid #dc3545');
        $('#id_tbus_dsc_pass').css('background-color', '#f8d7da');
        V_err++;
        V_txtErr += 'Contraseña no puede ser vacío.<br>';
    }else{
        if($("#id_tbus_dsc_pass").val().length <= 5) {
            $('#id_tbus_dsc_pass').css('border', '2px solid #dc3545');
            $('#id_tbus_dsc_pass').css('background-color', '#f8d7da');
            V_err++;
            V_txtErr += 'Contraseña debe tener un mínimo de 6 caracteres.<br>';
        }else{
            $('#id_tbus_dsc_pass').css('border', '2px solid #155724');
            $('#id_tbus_dsc_pass').css('background-color', '#d4edda');
        }
    }
    
    if(V_err > 0){
        $('#formValContReg').html(V_txtErr);
        $('#formValContReg').slideDown();
        return 1;
    }else{
        return 0;
    }
}