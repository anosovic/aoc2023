
for i in range(4,22):
	print(f"curl https://adventofcode.com/2023/day/{i} -H \"Cookie: session=53616c7465645f5f9224a5f37f79af736984a1fe0dbbe0fc917bd2b16b58615e1248f6ca84ead55f60f3e378f84777b0a7195f33e748d380ba8b7f9d1f928f79\" >> day{i:02}-problem.html")
	print(f"curl https://adventofcode.com/2023/day/{i}/input -H \"Cookie: session=53616c7465645f5f9224a5f37f79af736984a1fe0dbbe0fc917bd2b16b58615e1248f6ca84ead55f60f3e378f84777b0a7195f33e748d380ba8b7f9d1f928f79\" >> day{i:02}-input.txt")
