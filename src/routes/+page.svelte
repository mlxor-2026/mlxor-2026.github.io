<script>
	import Block from '$lib/components/Block.svelte';
	import GithubIcon from 'virtual:icons/mdi/github';
	import Person from '$lib/components/Person.svelte';
	import NavLink from '$lib/components/NavLink.svelte';
	import Intro from '../content/intro.md';
	import Call from '../content/call.md';
	import PCmembers from '../content/pc-members.md';
</script>

<svelte:head>
	<title>NeurIPS 2026 — Second Workshop on ML×OR: Mathematical Foundations and Operational Integration of Machine Learning for Uncertainty-Aware Decision-Making</title>
</svelte:head>

<div class="text-lg">
	<div class="flex w-full items-end justify-center font-serif">
		<div class="mx-8 w-full max-w-2xl pt-8 pb-8 text-black md:pt-28">
			<div class="mb-4 text-sm">
				<div class="inline-block rounded-md border border-black px-2 py-1 font-mono">
					NeurIPS 2026 WORKSHOP
				</div>
			</div>
			<div class="inline-block text-4xl"><strong>Second Workshop on ML×OR:</strong><br>Mathematical Foundations and Operational Integration of Machine Learning for Uncertainty-Aware Decision-Making</div>
			<div class="mt-8 flex items-center space-x-2">
				<div class="font-mono text-sm text-gray-500">Supported by</div>
				<div class="text-sm">INFORMS Applied Probability Society</div>
			</div>
			<div class="text-md mt-8 text-gray-800">December 2026</div>
			<div class="mt-2 text-sm text-gray-500">NeurIPS 2026 &middot;  Atlanta, GA, USA</div>
		</div>
	</div>
	<div
		class="sticky top-0 z-10 my-2 flex w-full items-start justify-center bg-gray-100/70 backdrop-blur-md md:py-1.5"
	>
		<div class="mx-8 w-full max-w-2xl select-none">
			<div
				class="my-2 flex flex-row flex-wrap items-center justify-start font-mono text-sm md:text-base"
			>
				<NavLink href="#call">Call for Papers</NavLink>
				<div class="mx-2 text-gray-400">/</div>
				<NavLink href="#schedule">Schedule</NavLink>
				<div class="mx-2 text-gray-400">/</div>
				<NavLink href="#speakers">Speakers</NavLink>
				<div class="mx-2 text-gray-400">/</div>
				<NavLink href="#organizers">Organizers & PC Members</NavLink>
			</div>
		</div>
	</div>

	<Block padding="py-8" class="md:text-justify">
		<Intro />
	</Block>
	
	<Block>
		<h1 class="mb-6 text-2xl font-bold" id="call">Call for Papers</h1>	
		<div class="md:text-justify">
		<Call />
		</div>
	</Block>

	<Block>
		<h1 class="mb-6 text-2xl font-bold" id="schedule">Schedule</h1>
		<div class="mb-6 text-base md:text-justify">
			<p>
				The tentative schedule is shown below and will be updated soon.
			</p>
		</div>
		<div>
			<table class="w-full border-collapse border border-gray-300 text-sm">
				<thead>
					<tr class="bg-gray-100">
						<th class="border border-gray-300 px-4 py-2 text-left whitespace-nowrap">Time</th>
						<th class="w-full border border-gray-300 px-4 py-2 text-left">Event</th>
					</tr>
				</thead>
				<tbody>
					<tr class="odd:bg-white even:bg-gray-50">
						<td class="border border-gray-300 px-4 py-2 whitespace-nowrap">8:30 &ndash; 9:00</td>
						<td class="w-full border border-gray-300 px-4 py-2"><strong>Keynote Talk 1</strong></td>
					</tr>
					<tr class="odd:bg-white even:bg-gray-50">
						<td class="border border-gray-300 px-4 py-2 whitespace-nowrap">9:00 &ndash; 10:00</td>
						<td class="w-full border border-gray-300 px-4 py-2"><strong>Poster Session 1</strong></td>
					</tr>
					<tr class="odd:bg-white even:bg-gray-50">
						<td class="border border-gray-300 px-4 py-2 whitespace-nowrap">10:00 &ndash; 10:30</td>
						<td class="w-full border border-gray-300 px-4 py-2">Coffee Break</td>
					</tr>
					<tr class="odd:bg-white even:bg-gray-50">
						<td class="border border-gray-300 px-4 py-2 whitespace-nowrap">10:30 &ndash; 11:15</td>
						<td class="w-full border border-gray-300 px-4 py-2"><strong>Panel Discussion 1</strong></td>
					</tr>
					<tr class="odd:bg-white even:bg-gray-50">
						<td class="border border-gray-300 px-4 py-2 whitespace-nowrap">11:15 &ndash; 11:55</td>
						<td class="w-full border border-gray-300 px-4 py-2"><strong>Spotlight Presentations</strong></td>
					</tr>
					<tr class="odd:bg-white even:bg-gray-50">
						<td class="border border-gray-300 px-4 py-2 whitespace-nowrap">11:55 &ndash; 12:45</td>
						<td class="w-full border border-gray-300 px-4 py-2">Lunch</td>
					</tr>
					<tr class="odd:bg-white even:bg-gray-50">
						<td class="border border-gray-300 px-4 py-2 whitespace-nowrap">12:45 &ndash; 13:45</td>
						<td class="w-full border border-gray-300 px-4 py-2"><strong>Poster Session 2</strong></td>
					</tr>
					<tr class="odd:bg-white even:bg-gray-50">
						<td class="border border-gray-300 px-4 py-2 whitespace-nowrap">13:45 &ndash; 14:15</td>
						<td class="w-full border border-gray-300 px-4 py-2"><strong>Keynote Talk 2</strong></td>
					</tr>
					<tr class="odd:bg-white even:bg-gray-50">
						<td class="border border-gray-300 px-4 py-2 whitespace-nowrap">14:15 &ndash; 14:45</td>
						<td class="w-full border border-gray-300 px-4 py-2">Coffee Break</td>
					</tr>
					<tr class="odd:bg-white even:bg-gray-50">
						<td class="border border-gray-300 px-4 py-2 whitespace-nowrap">14:45 &ndash; 15:45</td>
						<td class="w-full border border-gray-300 px-4 py-2"><strong>Poster Session 3</strong></td>
					</tr>
					<tr class="odd:bg-white even:bg-gray-50">
						<td class="border border-gray-300 px-4 py-2 whitespace-nowrap">15:45 &ndash; 16:15</td>
						<td class="w-full border border-gray-300 px-4 py-2"><strong>Keynote Talk 3</strong></td>
					</tr>
					<tr class="odd:bg-white even:bg-gray-50">
						<td class="border border-gray-300 px-4 py-2 whitespace-nowrap">16:15 &ndash; 17:00</td>
						<td class="w-full border border-gray-300 px-4 py-2"><strong>Panel Discussion 2</strong></td>
					</tr>
				</tbody>
			</table>
		</div>
		<div class="mt-4 text-sm text-gray-600 italic">
			<p>The program and times are tentative and subject to change. Speakers will be announced.</p>
		</div>
	</Block>

	<Block padding="pb-4">
		<h1 class="mb-4 text-2xl font-bold" id="speakers">Speakers & Panelists</h1>
		<p class="text-base text-gray-600">The following speakers and panelists are confirmed so far.</p>
	</Block>
	<Block>
		<div class="flex flex-col items-center justify-center">
			<div class="flex flex-wrap justify-center">
			<Person
				name="Erick Delage"
				affiliation="HEC Montréal"
				link="https://tintin.hec.ca/pages/erick.delage/"
				image="./imgs/erick-delage.jpg"
			></Person>
			<Person
				name="Nathan Kallus"
				affiliation="Cornell University"
				link="https://nathankallus.com/"
				image="./imgs/nathan.jpg"
			></Person>
			<Person
				name="David<br>Simchi-Levi"
				affiliation="MIT"
				link="https://slevi1.mit.edu/"
				image="./imgs/Simchi-Levi.jpg"
			></Person>
			<Person
				name="Milind Tambe"
				affiliation="Harvard University"
				link="https://teamcore.seas.harvard.edu/tambe/"
				image="./imgs/tambe.jpg"
				position="top"
			></Person>
			<Person
				name="Masatoshi Uehara"
				affiliation="OpenAI"
				link="https://www.masatoshiuehara.com/"
				image="./imgs/uehara.jpg"
				position="top"
			></Person>
			<Person
				name="Benjamin<br>Van Roy"
				affiliation="Stanford University"
				link="https://web.stanford.edu/~bvr/"
				image="./imgs/vanroy.jpg"
			></Person>
			<Person
				name="Amy Ward"
				affiliation="University of Chicago"
				link="https://voices.uchicago.edu/amyward/"
				image="./imgs/amy-ward.jpg"
				position="top"
			></Person>			
			<Person
				name="Yao Xie"
				affiliation="Georgia Institute of Technology"
				link="https://www2.isye.gatech.edu/~yxie77"
				image="/imgs/Yao_Xie.jpg"
				position="top"
			></Person>
			<Person
				name="Linwei Xin"
				affiliation="Cornell University"
				link="https://xin.engineering.cornell.edu/"
				image="./imgs/LinweiXin.jpg"
			></Person>
			<Person
				name="Lei Ying"
				affiliation="University of Michigan"
				link="https://leiying.engin.umich.edu/"
				image="./imgs/Ying_Lei.jpg"
			></Person>
			<Person
				name="Assaf Zeevi"
				affiliation="Columbia University"
				link="https://business.columbia.edu/faculty/people/assaf-zeevi"
				image="./imgs/assaf.jpg"
			></Person>
			</div>
		</div>
	</Block>

	<Block padding="pb-4">
		<h1 class="mb-4 text-2xl font-bold" id="organizers">Organizers</h1>
	</Block>
	<Block>
		<div class="flex flex-col items-center justify-center">
			<div class="flex flex-wrap justify-center">
			<Person
				name="Minshuo Chen"
				affiliation="Northwestern University"
				link="https://minshuochen.github.io/"
				image="./imgs/chen-minshuo.jpg"
			></Person>
			<Person
				name="Jing Dong"
				affiliation="Columbia University"
				link="https://www.columbia.edu/~jd2736"
				image="./imgs/jingdong.jpg"
			></Person>
			<Person
				name="Henry Lam"
				affiliation="Columbia University"
				link="https://www.engineering.columbia.edu/faculty-staff/directory/henry-lam"
				image="./imgs/henry-lam.jpg"
			></Person>
			<Person
				name="Karthyek Murthy"
				affiliation="University of Southern California"
				link="https://sites.google.com/site/karthyekswebpage/"
				image="./imgs/karthyek.jpg"
				position="top"
			></Person>
			<Person
				name="Min-hwan Oh"
				affiliation="Seoul National University"
				link="https://minoh.io/"
				image="./imgs/mho.webp"
			></Person>
			<Person
				name="Devavrat Shah"
				affiliation="MIT"
				link="https://devavrat.mit.edu/"
				image="./imgs/DevavratShah.jpg"
			></Person>
			<Person
				name="Renyuan Xu"
				affiliation="Stanford University"
				link="https://renyuanxu.github.io/"
				image="./imgs/renyuan.jpg"
			></Person>
			<Person
				name="Enlu Zhou"
				affiliation="Georgia Institute of Technology"
				link="https://www.enluzhou.gatech.edu/"
				image="./imgs/Enlu.jpg"
			></Person>
			</div>
		</div>
	</Block>

	<Block padding="pb-4">
		<h1 class="mb-4 text-2xl font-bold" id="program_committee">Program Committee Members</h1>
		<div class="text-base">
			<PCmembers />
		</div>
	</Block>

	<div class="mt-8 flex w-full justify-center bg-gray-100 pt-4 font-sans">
		<div class="mx-8 w-full max-w-3xl">
			<div class="flex w-full flex-col items-center justify-start">
				<div class="mt-4 mb-8 text-2xl text-gray-500">
					<a
						href="https://github.com/mlxor-2026/mlxor-2026.github.io"
						target="_blank"
						rel="noreferrer"
						class="mr-2"
					>
						<GithubIcon class="inline-block hover:text-black" />
					</a>
				</div>
			</div>
			<div class="mb-24 text-sm text-gray-600">
				This website is licensed under a <a
					class="underline"
					href="http://creativecommons.org/licenses/by-sa/4.0/"
					target="_blank"
					rel="noreferrer">Creative Commons Attribution-ShareAlike 4.0 International License</a
				>
				and is based on the
				<a class="underline" href="https://leela-interp.github.io/" target="_blank" rel="noreferrer"
					>Leela Interp</a
				> project. That means you're free to borrow the source code of this website with attribution.
			</div>
		</div>
	</div>
</div>
