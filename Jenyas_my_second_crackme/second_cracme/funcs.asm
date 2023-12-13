.code
	check_numbers_letters proc
		xor rax,rax
		xor r11,r11
		xor r12,r12
		xor r13,r13
		mov rsi,rcx
		run_let:
			mov bl,[rsi]
			cmp bl,'0'
			jl not_good_character
			cmp bl,'9'
			jg letter
			mov r11,1
			jmp next
			letter:
			cmp bl,'A'
			jl not_good_character
			cmp bl,'Z'
			jg letter2
			mov r12,1
			jmp next
			letter2:
			cmp bl,'a'
			jl not_good_character
			cmp bl,'z'
			jg not_good_character
			mov r13,1
			next:
			inc rsi
			cmp byte ptr[rsi],0
			jne run_let
		add r11,r12
		add r11,r13
		cmp r11,3
		je have_letters_and_digits
		not_good_character:
		xor rax,rax
		ret
		have_letters_and_digits:
		mov rax,1
		ret
	check_numbers_letters endp

	check_len proc
		xor rax,rax
		mov rsi,rcx
		run_len:
			cmp byte ptr[rsi],0
			je end_len
			inc rsi
			inc rax
			jmp run_len
		end_len:
		cmp rax,8
		jl not_good_len
		mov rax,1
		ret
		not_good_len:
		xor rax,rax
		ret
	check_len endp

	check_calc proc
		mov rsi,rcx
		mov r11b,17
		mov r12b,19
		mov r13b,25
		run_calc:
			mov bl,[rsi]
			cmp bl,'9'
			jg calc_letter1
			sub bl,47
			sub r11b,bl
			jmp next2
			calc_letter1:
			cmp bl,'Z'
			jg calc_letter2
			sub bl,64
			sub r12b,bl
			jmp next2
			calc_letter2:
			sub bl,'a'
			inc bl
			sub r13b,bl
			next2:
			inc rsi
			cmp byte ptr[rsi],0
			jne run_calc
		cmp r11b,0
		jne not_good_calc
		cmp r12b,0
		jne not_good_calc
		cmp r13b,0
		jne not_good_calc
		mov rax,1
		ret
		not_good_calc:
		xor rax,rax
		ret
	check_calc endp
end