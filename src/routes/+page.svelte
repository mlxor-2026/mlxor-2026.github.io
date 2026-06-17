<script>
	import Block from '$lib/components/Block.svelte';
	import GithubIcon from 'virtual:icons/mdi/github';
	import Person from '$lib/components/Person.svelte';
	import NavLink from '$lib/components/NavLink.svelte';
	import Intro from '../content/intro.md';
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
				<div class="font-mono text-sm text-gray-500">Theme</div>
				<div class="text-sm">Decision-Making with GenAI + OR</div>
			</div>
			<div class="text-md mt-8 text-gray-800">December 2026</div>
			<div class="mt-2 text-sm text-gray-500">NeurIPS 2026 &middot; Location to be announced</div>
		</div>
	</div>
	<div
		class="sticky top-0 z-10 my-2 flex w-full items-start justify-center bg-gray-100/70 backdrop-blur-md md:py-1.5"
	>
		<div class="mx-8 w-full max-w-2xl select-none">
			<div
				class="my-2 flex flex-row flex-wrap items-center justify-start font-mono text-sm md:text-base"
			>
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
		<h1 class="mb-6 text-2xl font-bold" id="schedule">Schedule</h1>
		<div class="mb-6 text-base md:text-justify">
			<p>
				The planned 8.5-hour program (8:30&ndash;17:00) consists of 3 keynote talks (30 mins each),
				2 panel discussions (45 mins each), 3 poster sessions (1 hour each), 4 spotlight
				presentations for selected submissions (10 mins each), and break times (2 30-min coffee
				breaks and a 50-min lunch). The tentative schedule is below.
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
		<h1 class="mb-4 text-2xl font-bold" id="organizers">Organizers</h1>
	</Block>
	<Block>
		<div class="flex flex-col items-center justify-center">
			<div class="flex flex-wrap justify-center">
			<Person
				name="Minshuo Chen"
				affiliation="Northwestern University"
				link="https://minshuochen.github.io/"
				image="https://minshuochen.github.io/self.jpg"
			></Person>
			<Person
				name="Jing Dong"
				affiliation="Columbia University"
				link="https://www.columbia.edu/~jd2736"
				image="https://www.columbia.edu/~jd2736/index_files/image004.jpg"
			></Person>
			<Person
				name="Henry Lam"
				affiliation="Columbia University"
				link="https://www.engineering.columbia.edu/faculty-staff/directory/henry-lam"
				image="https://www.engineering.columbia.edu/sites/default/files/styles/faculty_masthead_image/public/2024-07/Faculty-Henry_Lam-Thumbnail-435x435.jpg?itok=AqiJMvAi"
			></Person>
			<Person
				name="Karthyek Murthy"
				affiliation="University of Southern California"
				link="https://sites.google.com/site/karthyekswebpage/"
				image="./imgs/karthyek.jpg"
			></Person>
			<Person
				name="Min-hwan Oh"
				affiliation="Seoul National University"
				link="https://minoh.io/"
				image="https://minoh.io/assets/img/mho.webp"
			></Person>
			<Person
				name="Devavrat Shah"
				affiliation="MIT"
				link="https://devavrat.mit.edu/"
				image="https://devavrat.mit.edu/files/2025/05/cropped-DevavratShah.jpg"
			></Person>
			<Person
				name="Renyuan Xu"
				affiliation="Stanford University"
				link="https://renyuanxu.github.io/"
				image="https://renyuanxu.github.io/images/renyuan3.png"
			></Person>
			<Person
				name="Enlu Zhou"
				affiliation="Georgia Institute of Technology"
				link="https://www.enluzhou.gatech.edu/"
				image="https://enluzhou.gatech.edu/images/Enlu2017.jpg"
			></Person>
			</div>
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
				name="Assaf Zeevi"
				affiliation="Columbia University"
				link="https://business.columbia.edu/faculty/people/assaf-zeevi"
				image="https://business.columbia.edu/sites/default/files-efs/styles/default_content_image_cinema/public/person/photos/assaf-pic-19.jpg?h=6ef299b7&itok=09SgCMLG"
			></Person>
			<Person
				name="Erick Delage"
				affiliation="HEC Montréal"
				link="https://tintin.hec.ca/pages/erick.delage/"
				image="https://www.hec.ca/en/profs/erick.delage.jpg"
			></Person>
			<Person
				name="Masatoshi Uehara"
				affiliation="OpenAI"
				link="https://www.masatoshiuehara.com/"
				image="./imgs/uehara.jpg"
			></Person>
			<Person
				name="Yao Xie"
				affiliation="Georgia Institute of Technology"
				link="https://www2.isye.gatech.edu/~yxie77"
				image="/imgs/Yao_Xie.jpg"
			></Person>
			<Person
				name="Lei Ying"
				affiliation="University of Michigan"
				link="https://leiying.engin.umich.edu/"
				image="https://ecesite.engin.umich.edu/wp-content/uploads/sites/59/2021/08/Ying_Lei705.jpg"
			></Person>
			<Person
				name="Linwei Xin"
				affiliation="Cornell University"
				link="https://xin.engineering.cornell.edu/"
				image="https://xin.engineering.cornell.edu/files/2025/06/LinweiXin_Homepage_500x500-1.jpg"
			></Person>
			<Person
				name="Milind Tambe"
				affiliation="Harvard University"
				link="https://teamcore.seas.harvard.edu/tambe/"
				image="https://seas.harvard.edu/sites/default/files/styles/headshot_1x/public/2021-10/tambe_200x300_0.jpg?h=bf372811&itok=KuTphLLc"
			></Person>
			<Person
				name="David Simchi-Levi"
				affiliation="MIT"
				link="https://slevi1.mit.edu/"
				image="https://cee.mit.edu/wp-content/uploads/2021/07/Simchi-Levi.png"
			></Person>
			<Person
				name="Amy Ward"
				affiliation="University of Chicago"
				link="https://voices.uchicago.edu/amyward/"
				image="https://www.chicagobooth.edu/-/media/project/chicago-booth/faculty-and-insights/faculty/amy-ward/chicago-booth-amy-ward.jpg?cx=0.49&cy=0.48&cw=749&ch=940&hash=80829518B021A2530847E69CAEA35F80"
			></Person>
			<Person
				name="Benjamin Van Roy"
				affiliation="Stanford University"
				link="https://web.stanford.edu/~bvr/"
				image="https://web.stanford.edu/~bvr/photo.jpg"
			></Person>
			<Person
				name="Nathan Kallus"
				affiliation="Cornell University"
				link="https://nathankallus.com/"
				image="https://nathankallus.com/nathan.jpg"
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
