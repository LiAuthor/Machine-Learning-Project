<template>
    <div class="base">
        <div class="cube"></div>
        <div class="cube"></div>
        <div class="cube"></div>
        <div class="cube"></div>
        <div class="cube"></div>
        <div class="cube"></div>
        <div class="cube"></div>
        <div class="cube"></div>
        <div class="cube"></div>
    </div>
</template>

<style lang="scss" scoped>
.base {
	height: 9em;
	margin: -7.5em;
	margin-top: 3em;
	width: 9em;
	transform: rotateX(45deg) rotateZ(45deg);
	transform-style: preserve-3d;
	.cube,
	.cube:after,
	.cube:before {
		content: '';
		float: left;
		height: 3em;
		position: absolute;
		width: 3em;
	}
	.cube {
		background-color: #05afd1;
		position: relative;
		transform: translateZ(3em);
		transform-style: preserve-3d;
		transition: .25s;
		box-shadow: 13em 13em 1.5em rgba(0, 0, 0, 0.1);
		animation: anim 1s infinite;
		&:after {
			background-color: #049dbc;
			transform: rotateX(-90deg) translateY(3em);
			transform-origin: 100% 100%;
		}
		&:before {
			background-color: #048ca7;
			transform: rotateY(90deg) translateX(3em);
			transform-origin: 100% 0;
		}
		&:nth-child(1) {animation-delay: 0.05s;}
		&:nth-child(2) {animation-delay: 0.1s;}
		&:nth-child(3) {animation-delay: 0.15s;}
		&:nth-child(4) {animation-delay: 0.2s;}
		&:nth-child(5) {animation-delay: 0.25s;}
		&:nth-child(6) {animation-delay: 0.3s;}
		&:nth-child(7) {animation-delay: 0.35s;}
		&:nth-child(8) {animation-delay: 0.4s;}
		&:nth-child(9) {animation-delay: 0.45s;}
	}
	@keyframes anim {
		50% {
			transform: translateZ(0.5em);
		}
	}
}

</style>