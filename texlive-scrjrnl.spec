# revision 27810
# category Package
# catalog-ctan /macros/latex/contrib/scrjrnl
# catalog-date 2012-09-24 22:53:58 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-scrjrnl
Version:	0.1
Release:	6
Summary:	Typeset diaries or journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scrjrnl
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scrjrnl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scrjrnl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scrjrnl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A class, based on scrbook, designed for typesetting diaries,
journals or devotionals.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/scrjrnl/scrjrnl.cls
%doc %{_texmfdistdir}/doc/latex/scrjrnl/README
%doc %{_texmfdistdir}/doc/latex/scrjrnl/example.pdf
%doc %{_texmfdistdir}/doc/latex/scrjrnl/scrjrnl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/scrjrnl/scrjrnl.dtx
%doc %{_texmfdistdir}/source/latex/scrjrnl/scrjrnl.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
